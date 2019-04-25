=============================================================
Self-healing and auto-scaling with Heat, Mistral, Zaqar, Aodh
=============================================================

This use case describes an existing scenario for auto-scaling a
self-healing cluster.



OpenStack projects used
=======================

* Heat
* Mistral
* Zaqar
* Telemetry (Aodh, Pinko, Gnocchi)


Remediation class
=================

Reactive


Fault detection
===============

The self-healing scenario detect failure like when any instance in
cluster been delete, or updated out side of this automatic flow.


Inputs and decision-making
==========================

* A cluster builder (Heat):

  You can use Heat to build cluster, managing resource dependancies,
  plan some flexibility with batch action, and also reproducable to
  another OpenStack environment with same template. Whatever you're
  using for building cluster, you need to make sure it allow to your
  flow control service (Mistral) to trigger update and replace
  unhealthy node in cluster.

* A monitoring service (Aodh):

  There are multiple choices for self-healing monitors to monitor that
  cluster and notify queue service; you can absolutely replace any
  monitoring service in this showcase and use your own existing
  services. Just make sure you're able to monitoring nodes in cluster
  and able to send notification out when alarm triggered.

* A queue service (Zaqar):

  A queue or any services that accept notification from alarm service
  and capable to trigger healing flow.

* A triggerable flow control service (Mistral):

  A triggerable flow control service to run healing flow. Make sure
  your flow contains most cases. So we can guarantee that cluster is
  healed. Covering most successes and failure cases (as many as you
  can) is always a good idea.

We're using Heat, Aodh, Zaqar, and Mistral in this example. You can
always replace any service with your own services. Just make sure
they're fully integrated to each other for your healing scenario.


Remediation
===========

In our example, for each unit in the cluster, we set up a Nova
instance to run application on, binding that instance to a
load-balancer so the application can use lbaas in its infrastructure.

For healing, we create multiple event alarms monitoring the status of
that instance, a Zaqar queue for alarms to send notifications on, and
a Zaqar MistralTrigger (a resource type in Heat to use Zaqar
subscription to trigger Mistral workflow) to listen on that queue and
trigger Mistral workflow to mark this unit as unhealthy and then use
Heat stack update to replace unhealthy unit in cluster.

At this point you already got your structure for self-healing. As you
can see in the example, we are monitoring events like
``compute.instance.delete.*``.  If you also use Aodh, please make sure
the event you're monitoring is enabled from services and ceilometer
(be aware that some events are disabled by default).

The event alarm going to send a ``POST`` request to Zaqar queue if the
instance status changed to delete. Again, it's possible to use your
own alarm services.

Once Zaqar queue gets that information, it will trigger a Mistral
workflow. That workflow will mark that unit (in this case it's a
server with nginx) as unhealthy in Heat and trigger a stack
update. Heat will replace all unhealthy unit and regenerate one for
your cluster.


Existing implementation(s)
==========================

With ability to self-heal, you can (as we show in this case) combine
with autoscaling ability. Also as you can notice, we use Heat
container agent, so your image only need to support ability to run
container (instead of pre-install services with
diskimage-builder). Here is the example Heat template :doc:`sample
files <heat-mistral-aodh>`. Also here's link for relevant `slides
(with video link)
<https://www.slideshare.net/GuanYuLin1/autoscale-a-selfhealing-cluster-in-openstack-with-heat>`_.


Future work
===========

We need better support for scaling with some resources require trust.
All further work is tracked in `the story "Improve Autoscaling
integration with Self-healing"
<https://storyboard.openstack.org/#!/story/2003690>`_.  Also
integration with Vitrage is work in progress tracked in `the story
"Achieve Self healing with Vitrage Mistral And Heat"
<https://storyboard.openstack.org/#!/story/2002684>`_.
