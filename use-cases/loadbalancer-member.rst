..
  This template is intended to encourage a certain level of
  consistency between different use cases.  Adherence to the structure
  of this template is recommended but not strictly required.

  This template should be in ReSTructured text.  For help with syntax,
  see <http://sphinx-doc.org/rest.html>. To test out your formatting,
  see <http://www.tele3.cz/jbar/rest/rest.html>.

===============================
Load Balancer Member Respawning
===============================

..
  Please fill in the blanks in this use case statement, or rephrase
  as appropriate.

As a cloud operator, whenever a load balancer member node fails, I want the
load balancer to stop directing traffic to the failed member and for a new
member to be spawned.


Fault class
===========

..
  Please choose which of these classes are relevant and delete the
  others.  If you can think of a new class which should be listed
  here, please update the template.

* Hardware failure
* Software error
* Network failure


OpenStack projects used
=======================

..
  Please provide a list of projects (OpenStack and otherwise) which
  may be used in order to implement this use case.  If no
  implementation exists yet, suggestions are sufficient here.

* Openstack Aodh (telemetry alarm service)
* Openstack Heat (orchestration)
* Openstack Octavia (load balancer as a service)


Remediation class
=================

..
  Please choose which of these classes are relevant and delete the
  others.  If you can think of a new class which should be listed
  here, please update the template.

* Reactive


Fault detection
===============

From the `Octavia admin guide
<https://docs.openstack.org/octavia/latest/admin/guides/operator-maintenance.html#monitoring-pool-members>`_:

  Octavia will use the health information from the underlying load
  balancing application to determine the health of members. This
  information will be streamed to the Octavia database and made
  available via the status tree or other API methods.

In addition, an Aodh alarm is defined to detect load balancer member
node failure and trigger the alarm action to notify Heat.  This
``loadbalancer_member_health`` type alarm rule was `added to Aodh in
April 2019 <https://review.opendev.org/#/c/654221/>`_, and at the time
of writing a patch is under review to `add a Heat resource for
creating this alarm type automatically via Heat templates
<https://review.opendev.org/#/c/662381/>`_.  It is intended to update
this document later with sample Heat templates.


Inputs, decision-making, and remediation
========================================

..
  Describe how decisions about the remediation action are taken.  In
  particular list any other components or inputs which may provide
  additional context to help determine appropriate remediation of the
  fault.

* Octavia's builtin behavior automatically stops directing traffic to
  the unresponsive member node.
* Heat receives the Aodh alarm regarding the unresponsive member node,
  and according to the behavior defined in the stack template, spawns
  a new instance to replace the unresponsive member node.
* Octavia detects when the new member node is operational and begins
  directing some traffic to the new node.


Existing implementation(s)
==========================

..
  If there are one or more existing implementations of this use case,
  please give as many details as possible, in order that operators can
  re-implement the use case in their own clouds.  However any
  information is better than no information!  Linking to external
  documents is perfectly acceptable.

A demo video is available
`here <https://www.youtube.com/watch?v=dXsGnbr7DfM>`_.


Future work
===========

..
  Please link from here to any relevant specs.  If a cross-project
  spec is required, it can be placed under ../specs/ in this
  repository.


Dependencies
============

..
  - Include specific references to specs and/or blueprints in
    self-healing-sig, or in other projects, that this one either depends
    on or is related to.

  - Does this feature require any new library dependencies or code
    otherwise not included in OpenStack? Or does it depend on a specific
    version of library?
