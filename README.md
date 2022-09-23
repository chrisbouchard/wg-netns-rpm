# RPM Spec for wg-netns

[![Fedora Copr Build Status][copr-package-status-img]][copr-package]

[copr-package-status-img]: https://copr.fedorainfracloud.org/coprs/chrisbouchard/upliftinglemma/package/wg-netns/status_image/last_build.png
[copr-package]: https://copr.fedorainfracloud.org/coprs/chrisbouchard/upliftinglemma/package/wg-netns/


## Overview

This repository provides an RPM spec for [dadevel/wg-netns], which in the
package's own words is

> [wg-quick] with support for Linux network namespaces. A simple Python script
> that implements the steps described at [wireguard.com/netns].

The RPM provides the `wg-netns` script and the `wg-netns@.service` systemd
service unit.

[dadevel/wg-netns]: https://github.com/dadevel/wg-netns
[wg-quick]: https://git.zx2c4.com/wireguard-tools/about/src/man/wg-quick.8
[wireguard.com/netns]: https://www.wireguard.com/netns/#ordinary-containerization


## Installation

RPMs built from this spec are available from the [chrisbouchard/upliftinglemma]
repository on Fedora Copr. Assuming you're using a recent version of Fedora or
CentOS, you can install using `dnf`.

```console
$ dnf copr enable chrisbouchard/upliftinglemma
$ dnf install wg-netns
```

You may have to agree to some prompts if this is the first Copr repository
you've enabled.

[chrisbouchard/upliftinglemma]: https://copr.fedorainfracloud.org/coprs/chrisbouchard/upliftinglemma


## Contributing

I'm open to contributions, but remember that this repository is *only* for RPM
packaging. Any contributions related to wg-netns itself should be directed to
the upstream project.
