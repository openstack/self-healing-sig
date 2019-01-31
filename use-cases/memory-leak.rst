..

This work is licensed under a Creative Commons Attribution 3.0 Unported License.
http://creativecommons.org/licenses/by/3.0/legalcode

=============================================
Memory leak mitigation and failure prevention
=============================================

In a cloud infrastructure, it is important to detect and mitigate memory leaks
in critical infrastructure software before catastrophic failure takes place.


Problem description
===================

Many long-running software services are susceptible to memory leaks. A service
experiencing memory leak tends to gradually consume more and more memory
during its operation, ultimately compromising the performance and the
stability of the service. In the case of critical infrastructure software,
it is important to detect and prevent catastrophic failure due to memory
leaks.


Fault class
===========

  * Software error
  * Performance degradation


OpenStack projects used
=======================

There are at least three solution architectures.

1. Local: mitigation decisions and actions are conducted locally on each
   server.
2. Central: mitigation decisions and actions are orchestrated by a central
   service.
3. Delegated: mitigation decision policy can be defined centrally but
   localized to each server.


Local
-----
In the local architecture, a local utility can make the decision to restart a
process or take other mitigating actions when the process exceeds certain
fixed memory thresholds specified by the cloud operator. Candidate
implementations include:

- custom scripts.
- native memory limit mechanisms (e.g., cgroups) which would kill a process
  when memory usage becomes too high, allowing another mechanism to restart
  the process.
- `Monit`_.

.. _Monit: https://mmonit.com/monit/documentation/monit.html#Process-resource-tests


Central
-------
In the central architecture, mitigation decisions can be made at a central
level which is able to use cloud level information and policy not available at
a local level. Mitigation actions can include the orchestration of graceful
failovers that involve multiple servers.

There are three logical components to a solution.

* Memory usage collection:

  - Monasca (monasca-agent)
  - Nagios
  - Zabbix

* Mitigation decision:

  - Congress
  - Vitrage
  - Watcher

* Mitigation action:

  - Mistral
  - Watcher


Delegated
---------
The delegated architecture might be implemented as a mixture of the above two.


Remediation class
=================

  Proactive / preemptive


Fault detection
===============

Definitive detection of memory leak is an unsolved problem. For the purpose of
this use case, suspected memory leak can be determined based on operator-set
limits or a more generic procedure based on memory usage history and other
relevant information.


Inputs and decision-making
==========================

Inputs:
  * Memory usage by process.
  * Memory usage by server.
  * (Potentially) Memory usage history.
  * (Potentially) A list of candidate services or processes for memory leak
    mitigation.

Decision making:
  * The simplest case is when the operator prescribes memory limits for each
    relevant process. Take mitigating actions when prescribed memory limits
    for a service/process is breached.

  * The appropriate memory limits for each service/process might be determined
    by an inductive algorithm. The subject is under active investigation by
    the research community (for selected references, see `References`_).

  * When there are no prescribed memory limits, decisions can be made on the
    basis of a more generic procedure or policy. For example, a policy sketch
    may be as follows.

    - When a server's overall memory usage exceeds 90% of available memory for
      a period of 10 minutes, take mitigating actions on the candidate
      services or processes, prioritized by parameters such as:

      + Each service's total memory usage.
      + Each service's historical memory usage.
      + Risk and level of disruption of mitigating action taken upon each
        service.


Remediation
===========

Two main mitigating approaches are available:

  * Restart the service experiencing memory leak.
  * Orchestrate a graceful fail-over.

Existing implementation(s)
==========================

Existing implementations are available for the local architecture. See `Local`_.


Future work
===========

If there is operator interest in the central or delegated architectures,
future work would include implementing the architectures using the referenced
projects and documenting the results.


Dependencies
============

Not applicable.


References
==========

Matthias Hauswirth and Trishul M. Chilimbi. 2004.
Low-overhead memory leak detection using adaptive statistical profiling.
SIGOPS Oper. Syst. Rev. 38, 5 (October 2004), 156-164.
DOI=http://dx.doi.org/10.1145/1037949.1024412

Sor, Vladimir, Plumbr Ou, Tarvo Treier and Satish Narayana Srirama.
“Improving Statistical Approach for Memory Leak Detection Using Machine
Learning.” 2013 IEEE International Conference on Software Maintenance (2013):
544-547.
