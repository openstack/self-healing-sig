***********************
OpenStack testing tools
***********************

With the rapid expansion of OpenStack, a variety of tools have emerged
for testing different aspects of OpenStack.  However there is
currently no unified solution that can test availability, reliability,
performance, and scalability of OpenStack infrastructure.

The aim of this SIG is to create self-healing infrastructure, and in
order to move in to that direction there is a need for an automated
destructive/extreme testing framework for OpenStack infrastructure.
As there have already been several projects tackling various parts of
the challenge, one goal is to avoid duplication of effort and see how
we can take advantage of these already developed tools and come up
with a unified solution.

Here is list of tools and the testing features that are provided by
those (as of August 2019):

=================================== ======= ======= ======= =========== =========== =========== ============ ========== ========== ==============================================================================================================
        Tools/Features              Control Data    Storage Performance Scalability Concurrency Disruptions/ OpenStack  Report     Active community [#]_
                                    plane   plane   plane   testing     testing     testing     Failure      Deployment generation
                                    testing testing testing                                     injection
=================================== ======= ======= ======= =========== =========== =========== ============ ========== ========== ==============================================================================================================
Rally_ (Uses Tempest)               X                       X           X           X           X            X          X          `Medium <https://github.com/openstack/rally/graphs/contributors>`__
Yardstick_                          X       X       X       X           X           X                        X          X          `NA since May 2019 <https://git.opnfv.org/yardstick/stats/?period=m&ofs=10>`__
Tempest_                            X                       X                                                                      `High <https://opendev.org/openstack/tempest/commits/branch/master>`__
Shaker_                                     X               X                                                X          X          `Low <https://opendev.org/performa/shaker/commits/branch/master>`__
OS-Faults_                                                                                      X                                  `NA since July 2019 <https://opendev.org/performa/os-faults/commits/branch/master>`__
KloudBuster_                                X       X       X           X                                               X          `NA since June 2019 <https://github.com/openstack/kloudbuster/graphs/contributors>`__
HA-Failure-Test_ (Uses Tempest)     X                                                           X                                  `NA since November 2016 <https://github.com/avdhoot07/HA-Failure-TEST/graphs/contributors>`__
Cloud99_                            X       X                                                   X                       X          `NA since May 2017 <https://github.com/cisco-oss-eng/Cloud99/graphs/contributors>`__
Browbeat_ (Uses Rally and Shaker)   X       X               X           X                                    X                     `High <https://github.com/cloud-bulldozer/browbeat/graphs/contributors>`__
Harbinger_                                  X       X                                                                              `Low <https://github.com/att-comdev/harbinger/graphs/contributors>`__
Enos_ (Uses Rally and Shaker)       X       X               X                                                X          X          `NA since May 2019 <https://github.com/BeyondTheClouds/enos/graphs/contributors>`__
Chaostoolkit-openstack_                                                                         X                       X          `NA since April 2019 <https://github.com/chaostoolkit-incubator/chaostoolkit-openstack/graphs/contributors>`__
Jepsen_ (not specific to OpenStack)                                                             X                       X          `High <https://github.com/jepsen-io/jepsen/graphs/contributors>`__
OPNFV-Doctor_                                                                                   X                                  `NA since April 2019 <https://gerrit.opnfv.org/gerrit/gitweb?p=doctor.git;a=summary>`__
Stepler_ (Uses OS-faults)                                                                       X                                  `NA since February 2019 <https://github.com/Mirantis/stepler/graphs/contributors>`__
NFVbench_                                   X       X       X           X                                               X          `Medium <https://github.com/opnfv/nfvbench/graphs/contributors>`__
VMTP_                                       X               X                                                           X          `Low <https://opendev.org/x/vmtp/commits/branch/master>`__
Eris_ (In development)              X       X               X           X           X           X                       X          `NA since November 2017 <https://github.com/LCOO/eris>`__
=================================== ======= ======= ======= =========== =========== =========== ============ ========== ========== ==============================================================================================================

.. [#] Commits per month: Low<5, Medium<15, High=>15, NA=No Activity

.. _Rally:

`Rally <https://rally.readthedocs.io/en/latest/overview/overview.html#use-cases>`__
===================================================================================

-  Deployment of OpenStack
-  Verification of deployment
-  Benchmarking: Simulate real user load
-  Profiler for scaling and performance issues
-  Report generation: Processing and aggregation of results

De-facto control plane performance testing, allows to create different
kind of tests including functional, concurrency, regression, load, scale
capacity and chaos testing.

.. _Yardstick:

`Yardstick <https://wiki.opnfv.org/display/yardstick/Yardstick>`__
==================================================================

-  Deployment
-  Run compute, storage, network test scenarios using a runner
-  Report generation with the following metrics:

   -  Performance/Speed
   -  Capacity/Scale
   -  Availability/Reliability

Inspired by Rally, was developed mainly from the prespective of
VNF(Virtual Network Function), but is a generic framework for testing
scenarios in OpenStack for performance, scalability and
availability/reliability.

.. _Tempest:

`Tempest <https://docs.openstack.org/tempest/latest/overview.html#tempest-the-openstack-integration-test-suite>`__
==================================================================================================================

-  Integration testing for live OpenStack
-  Test OpenStack publicly available API and scenarios that demonstrate
   a working cloud
-  Load testing possible as well

Mainly used for integration testing but non-functional testing
possible as well.

.. _Shaker:

`Shaker <https://pyshaker.readthedocs.io/en/latest/index.html>`__
=================================================================

-  Deploy instances and network in different topologies or network
   configurations using Heat
-  Run network related test scenarios
-  Report generation

Network load generation, testing and benchmarking. Based on 'iperf(3)'
and 'netperf' -> network testing topologies.

.. _OS-Faults:

`OS-Faults <https://github.com/openstack/os-faults>`__
======================================================

-  Library for initiating or terminating service/node/container/network
   as a way for introducing fault injections.
-  Allows for both hardware and software level faults

Used by Rally to introduce faults.

.. _KloudBuster:

`KloudBuster <https://github.com/openstack/kloudbuster>`__
==========================================================

-  Benchmarking of data plane and storage services in OpenStack

A fully integrated framework which is easy to use with basic knowledge
of OpenStack.

.. _HA-Failure-Test:

`HA-Failure-Test <https://github.com/avdhoot07/HA-Failure-TEST>`__
==================================================================

-  High Availability testing of OpenStack components
-  Set of Tempest scripts to test HA of components in HA cluster.
-  Stop service(s), perform sanity and verify

.. _Cloud99:

`Cloud99 <https://github.com/cisco-oss-eng/Cloud99>`__
======================================================

-  Monintoring: Nodes and services
-  Disruptions: in services, node, containers can be parallel,
   sequential or round robin
-  Runner: Perform actual tests with disruptions
-  All 3 runs as seperate threads and parallel

Makes use of Rally runner.

.. _Browbeat:

`Browbeat <https://github.com/cloud-bulldozer/browbeat>`__
==========================================================

-  Performance and scalability testing
-  Create Rally work loads
-  Run Shaker for network configuration, benchmarking and testing
-  CI and deployment: Can be used for CI or deploying data analysis
   tools.

.. _Harbinger:

`Harbinger <https://harbinger-dpm.readthedocs.io/en/latest/what/index.html>`__
==============================================================================

-  Manager for data plane testing frameworks in OpenStack
-  Can similtaneously execute multiple testing frameworks (Shaker,
   Yardstick)

.. _Enos:

`Enos <https://enos.readthedocs.io/en/stable/>`__
=================================================

-  Deployment of OpenStack on VMs or bare metal
-  Setup with different configurations
-  Benchmarking:

   -  Rally scenario for control plane
   -  Shaker scenario of data plane

-  Report generation: Get metrics/reports in Grafana

.. _Chaostoolkit-openstack:

`chaostoolkit-openstack <https://github.com/chaostoolkit-incubator/chaostoolkit-openstack>`__
=============================================================================================

-  Driver to perform set of actions and probes.

A minimal chaostoolkit driver for OpenStack compute resources.

.. _Jepsen:

`Jepsen <https://github.com/jepsen-io/jepsen>`__
================================================

-  Introduction of disruptions/faults
-  Testing
-  Report generation
-  Checkers for analyzing history

Not specific to OpenStack but general library for distributed systems,
written in Clojure.

.. _OPNFV-Doctor:

`OPNFV Doctor <https://wiki.opnfv.org/display/doctor/Doctor+Home>`__
====================================================================

-  Fault management and maintenance in VIM(Virtualized Infrastructure
   Manager) e.g OpenStack
-  Fault monitoring (Hardware, Hypervisor, Host OS faults)
-  Fault notification
-  Failure recovery (Switch to STBY config.)

.. _Stepler:

`Stepler <https://stepler.readthedocs.io/>`__
=============================================

-  Destructive testing
-  Test the availability of OpenStack cluster incase of node/service
   failure(s)

Make use of os-faults.

.. _NFVbench:

`NFVbench <https://opnfv-nfvbench.readthedocs.io/en/latest/testing/user/userguide/index.html>`__
================================================================================================

-  Measure network performance in OpenStack
-  Data plane performance testing
-  Benchmarking NFVi platforms and packet paths that are critical for NFV workloads

Adjusted more for NFV workloads.

.. _VMTP:

`VMTP <https://vmtp.readthedocs.io/en/latest/>`__
=================================================

-  Benchmarking VM to VM data path performance measurement
-  Latency measurement
-  TCP/UDP throughput measurement

Similar to NFVbench but more adapted towards enterprise workloads.

.. _Eris:

`Eris <https://docs.openstack.org/self-healing-sig/latest/eris/index.html>`__
=============================================================================

-  Control and data plane performance testing
-  High Availability testing
-  Scalability Testing
-  Concurrency Testing
-  Benchmarking and results generation

