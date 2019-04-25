..
  This template is intended to encourage a certain level of consistency
  between different use cases.  However strict adherence to the structure
  of this template is not required.

  This template should be in ReSTructured text. The filename in the git
  repository should match the launchpad URL, for example a URL of
  https://blueprints.launchpad.net/self-healing-sig/+spec/awesome-thing should be named
  awesome-thing.rst .  Please do not delete any of the sections in this
  template.  If you have nothing to say for a whole section, just write: None
  For help with syntax, see http://sphinx-doc.org/rest.html
  To test out your formatting, see http://www.tele3.cz/jbar/rest/rest.html

=======================================
The title of your self-healing use case
=======================================

..
  Please fill in the blanks in this use case statement, or rephrase
  as appropriate.

As a cloud operator, whenever one of my cloud's ________ has a _______
failure, I want to be notified of all affected _______.  Moreover, I
want _______ in order that ________ will continue to function.


Problem description
===================

..
  A more detailed description of the fault management scenario;
  however it is not advised to duplicate details covered in the
  sections below.  If the problem is not too complex, it may be more
  appropriate to simply delete this section and provide the details in
  the sections below.


Fault class
===========

..
  Please choose which of these classes are relevant and delete the
  others.  If you can think of a new class which should be listed
  here, please update the template.

  Hardware failure
  Software error
  Performance degradation


OpenStack projects used
=======================

..
  Please provide a list of projects (OpenStack and otherwise) which
  may be used in order to implement this use case.  If no
  implementation exists yet, suggestions are sufficient here.

* Zabbix
* Vitrage
* Mistral


Remediation class
=================

..
  Please choose which of these classes are relevant and delete the
  others.  If you can think of a new class which should be listed
  here, please update the template.

  Proactive / preemptive
  Predictive
  Reactive


Fault detection
===============

..
  Describe the exact nature of the fault, which components
  will be needed to automatically detect it, and how they
  should be configured or used for the detection.

  This may include details about relevant log streams, alarms,
  error codes etc.


Inputs and decision-making
==========================

..
  Describe how decisions about the remediation action are taken.  In
  particular list any other components or inputs which may provide
  additional context to help determine appropriate remediation of the
  fault.


Remediation
===========

..
  Describe how the fault may be remediated.  If there may be different
  approaches available, please list them all.


Existing implementation(s)
==========================

..
  If there are one or more existing implementations of this use case,
  please give as many details as possible, in order that operators can
  re-implement the use case in their own clouds.  However any
  information is better than no information!  Linking to external
  documents is perfectly acceptable.


Future work
===========

..
  Please link from here to any relevant specs.  If a cross-project
  spec is required, it can be placed under ../specs/ in this
  repository.

  Please also make sure that any linked specs contain back-links
  to this use case for maximum discoverability.


Dependencies
============

..
  - Include specific references to specs and/or blueprints in
    self-healing-sig, or in other projects, that this one either depends
    on or is related to.

  - Does this feature require any new library dependencies or code
    otherwise not included in OpenStack? Or does it depend on a specific
    version of library?
