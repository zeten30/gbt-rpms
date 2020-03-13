Name: gbt
Version: 2.0
Release: 2
Summary: Highly configurable prompt builder for Bash and ZSH written in Go
Group: Applications/System
BuildRoot: %buildroot
License: MIT
Vendor: Jiri Tyr <https://jtyr.io>
URL: https://github.com/jtyr/gbt
Source0: gbt.tar.gz
%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}


%description
Highly configurable prompt builder for Bash and ZSH written in Go


%prep
%setup -q -n gbt


%build
# noop


%install
%{__install} -d -m755 %{buildroot}/usr/bin/
%{__cp} -pr bin/gbt  %{buildroot}/usr/bin/

%{__install} -d -m755 %{buildroot}/usr/share/gbt/
%{__cp} -pr sources %{buildroot}/usr/share/gbt/
%{__cp} -pr themes %{buildroot}/usr/share/gbt/

%{__install} -d -m755 %{buildroot}/usr/share/doc/gbt/
%{__cp} -pr LICENSE %{buildroot}/usr/share/doc/gbt/LICENSE
%{__cp} -pr README.md %{buildroot}/usr/share/doc/gbt/README.md


%clean
# noop


%files
%license LICENSE
%defattr(-,root,root,-)
/usr/bin/gbt
/usr/share/gbt/
/usr/share/doc/gbt/


%changelog
* Mon Oct 21 2019 Milan Zink <zeten30@gmail.com> - 2.0-1
- initial gbt rpm release
