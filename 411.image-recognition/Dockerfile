FROM public.ecr.aws/lambda/python:3.10


# Copy requirements.txt
ADD ./ ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip3 install -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "function.handler" ]

