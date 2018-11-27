:orphan:

=============================================
Contributing to OpenStack's self-healing SIG
=============================================

If you would like to participate in discussions or contribute in any
way to the design and development of self-healing in OpenStack, please
first see the following wiki to understand the SIG's mission, scope,
and other supporting information:

  https://wiki.openstack.org/wiki/Self_healing_SIG

Many forms of contribution are valuable to the community, including but not
limited to the following:

- `Documentation of use cases <#use-cases>`_, including implementation details if available
- `Design specs`_
- `Code`_
- `Discussions`_ on all the above and other topics

Everyone is warmly encouraged to get involved in whatever capacity you
see fit.

Discussions
-----------

Discussions take place:

- on `the openstack-discuss mailing list
  <http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-discuss>`_
  with ``[self-healing-sig]`` in the Subject header,
- the `#openstack-self-healing IRC channel on Freenode
  <http://eavesdrop.openstack.org/irclogs/%23openstack-self-healing/>`_
  (including `meetings every fortnight
  <http://eavesdrop.openstack.org/#Self-healing_SIG_Meeting>`_),
- `the SIG's storyboard
  <https://storyboard.openstack.org/#!/project/openstack/self-healing-sig>`_,
- and in patch reviews.

Links to all resources can also be found in the `SIG wiki section on
community`_.

.. _`SIG wiki section on community`: https://wiki.openstack.org/wiki/Self-healing_SIG#Community_Infrastructure_.2F_Resources

Use cases
---------

The SIG serves to facilitate the discussion and documentation of self-healing
use cases at all stages of development from a seed idea to a fully tested use
case.

To call attention to a use case, please start the discussion in `one
of the established communication channels <#discussions>`_.

Alternatively, directly submit a patch to document the use case,
following the format laid out in the `template file
<http://git.openstack.org/cgit/openstack/self-healing-sig/tree/use-cases/template.rst>`__
in `the use-cases/ directory
<http://git.openstack.org/cgit/openstack/self-healing-sig/tree/use-cases>`_
of `the self-healing-sig repository
<http://git.openstack.org/cgit/openstack/self-healing-sig>`_.

See `Submitting a change`_ for more information.

Design specs
------------

Design specs are proposed implementations of self-healing
functionality across projects. To author a new design spec, please
follow the format laid out in the `template file
<http://git.openstack.org/cgit/openstack/self-healing-sig/tree/specs/template.rst>`__
in `the specs/ directory
<http://git.openstack.org/cgit/openstack/self-healing-sig/tree/specs>`_
of `the self-healing-sig repository`_.

See `Submitting a change`_ for more information.

Code
----

`The self-healing-sig repository`_ also holds any relevant
cross-project code, tests, and documentation that do not naturally
belong in a single project repository.

See `Submitting a change`_ for more information.

Submitting a change
-------------------

To submit a change to this repository, please follow the steps in this page:

   http://docs.openstack.org/infra/manual/developers.html

If you already have a good understanding of how the system works and your
OpenStack accounts are set up, you can skip to the development workflow
section of this documentation to learn how changes to OpenStack should be
submitted for review via the Gerrit tool:

   http://docs.openstack.org/infra/manual/developers.html#development-workflow

Pull requests submitted through GitHub will be ignored.
