===============================
Vitrage and Mistral Integration
===============================

Overview
========

Self-healing and fast recovery in real world cloud systems is challenging...

* Failures happen in real distributed systems
* A single failure may affect many resources
* We can see symptoms but it’s hard to find the root cause
* Recovery might be complicated

The integration of Vitrage and Mistral can help identifying the root cause and
taking corrective actions, in an end-to-end self-healing scenario.

Vitrage is the OpenStack Root Cause Analysis service for organizing, analyzing
and visualizing OpenStack and external alarms. It is used to provide insights
about the root cause of problems and deduce their existence before they are
directly reported.

Mistral is the OpenStack workflow service. It aims to provide a mechanism to
define tasks and workflows without writing code, manage and execute them in the
cloud environment.


Use Cases
=========

The integration of Vitrage with Mistral supports two kinds of use cases:

* Automatic workflow execution, based on predefined conditions
* Manual workflow execution from Vitrage Entity Graph (WIP in Rocky)


Use Case 1: NIC failure causes automatic instance migration
-----------------------------------------------------------

*"As a cloud operator, whenever one of my cloud's compute nodes has a NIC
failure, I want to be notified of all affected resources including instances
and applications. Moreover, I want the failed instances to be migrated away to
another hardware."*

In a complex system, a failure in one resource can have a wide effect on other
resources. One example is a NIC failure, that may cause the host, as well as
all instances running on it, to become unreachable. This may also affect
applications that are using these instances and lose their high-availability.

To identify the failed resources, the cloud operator can use Vitrage. Vitrage
will be notified by an external monitor (such as Zabbix) about the failed NIC.
Based on its cloud topology awareness, Vitrage will raise additional alarms on
the host, instances and affected applications.

An affected application will most likely be running in HA mode, so it will
perform a fail-over to the standby instance. However, it will lose its
high-availability. In order to fix it, Vitrage can execute a Mistral workflow
that will migrate the failed instance to a different host, so the application
will get back to a fully-operational state.

.. figure:: ./vitrage_and_mistral.png
   :scale: 100 %
   :align: center
   :alt: alternate text

Use Case 2: NIC failure with an optional manual instance migration
------------------------------------------------------------------

*"As a cloud operator, whenever one of my cloud's compute nodes has a NIC
failure, I want to be notified of all affected resources including instances
and applications. I then want an easy way to manually migrate a failed
instance to another compute and track its state."*

This is currently WIP in Rocky.

The use case is similar to use case 1, but in this use case the cloud operator
did not pre-configured Vitrage to execute a Mistral workflow when an
application is affected by an instance being unreachable.

As a result of a NIC failure, Vitrage raises alarms on the host, its instances
and the applications that are using them. The cloud operator can see this
information in Vitrage Entity Graph, locate a failed instance that affects an
application, and ask to execute a VM-migration Mistral workflow on that
instance.


Technical Details
=================

Vitrage ``evaluator templates`` define the business logic and the way that
Vitrage handles alarms and resource states. A template contains ``scenarios``,
where each scenario is made of ``condition`` and ``actions``.

Among other actions (like raise an alarm or modify the state of a resource),
the cloud operator can ask to execute a Mistral workflow with certain
parameters. For example, the cloud operator can define this scenario:

* ``condition:`` an application contains an instance that is unreachable
* ``action:`` execute a Mistral VM-Migration workflow on that instance

More details about Vitrage template definitions can be found here_

.. _here: https://docs.openstack.org/vitrage/latest/contributor/vitrage-template-format.html


Note that Vitrage could call Nova evacuate directly for the failed instance,
but using a Mistral workflow is a much more robust option. Mistral can track
the Nova evacuation process, check its status and verify that everything worked
as expected.


References
==========

- https://www.openstack.org/videos/sydney-2017/advanced-fault-management-with-vitrage-and-mistral

- https://wiki.openstack.org/wiki/Vitrage

- https://docs.openstack.org/mistral/latest/
