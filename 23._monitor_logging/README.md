# Monitoring & Logging
Today we look at how to observe what is happening inside your running system. The outcome should be that your group has a monitoring setup with Prometheus and Grafana running alongside your application, giving you visibility into the health and performance of your services.

## Learning Goals

* Understand the difference between monitoring and logging and why both matter.
* Set up Prometheus to scrape metrics from your application.
* Visualize metrics in Grafana with dashboards.
* Apply the second DevOps principle of **Feedback** by making the system's behavior visible to the team.

## Before Class

Read up on the core concepts:

* [What is Prometheus?](https://prometheus.io/docs/introduction/overview/)
* [What is Grafana?](https://grafana.com/docs/grafana/latest/introduction/)

Think about what you would want to monitor in your own project — what does "healthy" look like for your application?

## Todays Teachings

We start out by having a look at the theory behind monitoring and observability.

Then we will go through a practical setup:

* [Setting up Prometheus and Grafana](01._prometheus_grafana_setup.md)

And you will apply it to your own project:

* [Monitoring in your own project](02._cookbook_monitoring.md)

Setting this up at azure:

* [Monitoring a multi-VM deployment on Azure](03._azure_multivm_monitoring.md)
