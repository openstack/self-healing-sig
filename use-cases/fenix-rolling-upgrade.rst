==============================================
Infrastructure rolling maintenance and upgrade
==============================================

Telco has for years made maintenance and upgrades in rolling fashion. Now it is
the time to achieve this in the OpenStack also. Rolling upgrade makes minimal
downtime to infrastructure as well as for the application on top of it.


Problem description
===================

- Infrastructure maintenance and upgrade needs to possible in rolling fashion
  to minimize downtime for services and applications.

- Maintenance and upgrade needs to be managed without adding more resources
  to a system while all compute capacity is in use.

- It needs to be possible to know what hosts and instances are maintained and
  what not.

- There needs to be a generic messaging defined between infrastructure and
  application manager (VNFM).

- It has to be possible to ask application manager to scale down at non busy
  hour to get free capacity during rolling maintenance and upgrade.

- Application manager will need to know when planned maintenance session is
  over, so it can scale back to full capacity.

- Application manager needs to be aware of planned host maintenance, so
  application (VNF) will safely be running somewhere else when the host will
  be down for maintenance.

- Different infrastructure services needs to be aware of host being down for
  maintenance. This can be important to disable automatic self-healing
  actions or billing. There needs to be a generic messaging defined for this.

- Application manager needs to know when his instances are to move to
  upgraded host, so it can also make its own upgrade to take new
  capabilities into use.

- Rolling maintenance framework needs to be pluggable to handle different
  maintenance and upgrade workflows and actions for hosts. This is also
  important to support different payloads and clouds.

- Infrastructure admin needs to be able to have rolling maintenance done
  with one-click.

- Infrastructure admin needs to be able to know rolling maintenance status
  through API and notification.

- It must be possible for each maintenance session to define needed software
  packages and plug-ins to run the maintenance workflow properly.


OpenStack projects used
=======================

All mentioned problems are being solved by the new `Fenix
<https://wiki.openstack.org/wiki/Fenix>`_ project to manage the
rolling maintenance and upgrade. More of its internals can be read
from project own documentation and blueprints. Proof of concept code
is already being tested in the OPNFV Doctor CI with a sample
implementation. The `Doctor maintenance design document`__ describes
the initial interaction needed. Also, the presentation in the
OpenStack Vancouver summit `"How to gain VNF zero downtime during
Infrastructure Maintenance and Upgrade"`__ will show the way for
implementing the Fenix.

__ https://wiki.opnfv.org/download/attachments/5046291/Planned%20Maintenance%20Design%20Guideline.pdf?version=1&modificationDate=1527183603000&api=v2
__ https://www.openstack.org/videos/vancouver-2018/how-to-gain-vnf-zero-down-time-during-infrastructure-maintenance-and-upgrade

As Fenix can interact with the application manager. There is a
blueprint to support the interaction in Tacker__.  This would enable a
complex test case to be built to test Fenix workflow, that uses purely
OpenStack components.

__ https://blueprints.launchpad.net/tacker/+spec/vnf-rolling-upgrade

To disable self-healing, Fenix host maintenance notification could be
supported by Vitrage and Masakari.

As workflows can be different, there has already been some discussion with
the Airship and the Blazar projects. The Blazar should make a blueprint to have
it possible to change application-specific reservations to support rolling
maintenance. Airship could later look to implement its own maintenance and
upgrade process by utilizing Fenix.

Upgrade checks for different projects are `a community goal for
Stein`__. This is one step towards the automated rolling upgrade.

__ https://storyboard.openstack.org/#!/story/2003657


Future work
===========

`Fenix blueprints`__ indicate what is yet to be done for the basic
Fenix engine. When this work is ready, one can concentrate to make the
sample workflow plug-in for the rolling upgrade, sample upgrade action
plug-ins and the framework for testing it. Ideally, the framework use
case would be the OpenStack and application (VNF) upgrade. This can
then work as an example to implement own workflow and other plug-ins
for a specific real work use case.

__ https://storyboard.openstack.org/#!/worklist/482
