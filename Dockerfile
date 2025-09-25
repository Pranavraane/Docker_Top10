FROM python:3.11-slim

# Install tools for exploration
RUN apt-get update && \
    apt-get install -y curl nmap iputils-ping && \
    apt-get clean
RUN pip install jinja2==3.0.3


# Default shell (you can override on run)
CMD ["/bin/sh"]
