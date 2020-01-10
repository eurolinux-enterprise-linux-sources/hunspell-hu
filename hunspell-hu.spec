Name: hunspell-hu
Summary: Hungarian hunspell dictionaries
Version: 1.6.1
Release: 5%{?dist}
Source: http://downloads.sourceforge.net/magyarispell/hu_HU-%{version}.tar.gz
Group: Applications/Text
URL: http://magyarispell.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+ or GPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
Hungarian hunspell dictionaries.

%prep
%setup -q -n hu_HU-%{version}

%build
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_hu_HU.txt LEIRAS.txt
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar 31 2010 Caolan McNamara <caolanm@redhat.com> - 1.6.1-1
- latest version

* Sat Feb 06 2010 Caolan McNamara <caolanm@redhat.com> - 1.6-1
- latest version

* Thu Nov 05 2009 Caolan McNamara <caolanm@redhat.com> - 1.5-2
- source audit shows content changed silently upstream

* Thu Sep 17 2009 Caolan McNamara <caolanm@redhat.com> - 1.5-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 23 2008 Caolan McNamara <caolanm@redhat.com> - 1.4-1
- latest version

* Mon Mar 17 2008 Caolan McNamara <caolanm@redhat.com> - 1.3-1
- latest version

* Mon Nov 05 2007 Caolan McNamara <caolanm@redhat.com> - 1.2.2-1
- latest version

* Tue Oct 02 2007 Caolan McNamara <caolanm@redhat.com> - 1.2.1-1
- latest version

* Fri Aug 03 2007 Caolan McNamara <caolanm@redhat.com> - 1.2-2
- clarify that this is tri-licenced

* Fri Jun 01 2007 Caolan McNamara <caolanm@redhat.com> - 1.2-1
- next version

* Sat May 05 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.1-1
- latest canonical version

* Wed Feb 14 2007 Caolan McNamara <caolanm@redhat.com> - 0.20061105-2
- match licence

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20061105-1
- initial version
