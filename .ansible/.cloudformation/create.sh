
#!/bin/bash
############################################################
# Cloudformation Management                                #
############################################################
runCloudformation()
{
    state=$(aws cloudformation $1 --stack-name $2 --template-body file://$3.yml  --parameters file://$3-parameters.json --capabilities "CAPABILITY_IAM" "CAPABILITY_NAMED_IAM" --region=$AWS_REGION 2>&1)
    already_exists=$(echo "$state" | grep -F AlreadyExistsException)
    no_new_updates=""
    if [ ! -z "$already_exists" ] ; then
        echo "$2 already exists, Updating..."
        state=$(aws cloudformation update-stack --stack-name $2 --template-body file://$3.yml  --parameters file://$3-parameters.json --capabilities "CAPABILITY_IAM" "CAPABILITY_NAMED_IAM" --region=$AWS_REGION 2>&1)
    fi
    no_new_updates=$(echo "$state" | grep -F "No updates are to be performed")
    if [ ! -z "$no_new_updates" ] ; then
        echo "$2 Has no updates to be performed."
        return 0
    fi
    >&2 echo $state

}
############################################################
# Hold until network stack is created                      #
############################################################
STACK_STATUS="temp"
sleep_cnt=0
Hold()
{
    while [ $STACK_STATUS != "CREATE_COMPLETE" ] && [ $STACK_STATUS != "UPDATE_COMPLETE" ] ; do
        echo "Waiting for $2 stack to finalize..."
        STACK_STATUS=$(aws cloudformation describe-stacks --stack-name $1 --query Stacks[].StackStatus --output text)
        sleep 10
        echo $STACK_STATUS
        sleep_cnt=$((sleep_cnt+1))
        if [ $sleep_cnt -gt 100 ]; then 
            >&2 echo "FAILED: Stack took too long to finalize"
            break
        fi
    done
    echo "$2 Stack Completed"
}
############################################################
# Process the input options.                               #
############################################################
STACK_NAME=udgram-asg-$RANDOM
runCloudformation create-stack $STACK_NAME "asg"
Hold $STACK_NAME "Servers"
