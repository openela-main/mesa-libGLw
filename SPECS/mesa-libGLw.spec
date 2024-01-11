Summary: Xt / Motif OpenGL widgets
Name: mesa-libGLw
Version: 8.0.0
Release: 18%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://www.mesa3d.org
# archived project
%global gitver b060a0782f09ebe4f60c8fd4564c11ba043c331f
Source0: https://gitlab.freedesktop.org/mesa/glw/-/archive/%{gitver}/glw-%{gitver}.tar.bz2

BuildRequires: libXt-devel
BuildRequires: libGL-devel
%if 0%{?rhel}
BuildRequires: openmotif-devel
%else
BuildRequires: motif-devel
%endif
BuildRequires: autoconf automake libtool

Provides: libGLw

%description
Mesa libGLw runtime library.

%package devel
Summary: Mesa libGLw development package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libGL-devel
%if 0%{?rhel}
Requires: openmotif-devel
%else
Requires: motif-devel
%endif
Provides: libGLw-devel

%description devel
Mesa libGLw development package.

%prep
%setup -q -n glw-%{gitver}

%build
autoreconf -f -i -v
%configure --disable-static --enable-motif
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name \*.la | xargs rm -f

%check

%ldconfig_post
%ldconfig_postun

%files
%doc README
%{_libdir}/libGLw.so.1
%{_libdir}/libGLw.so.1.0.0

%files devel
%{_libdir}/libGLw.so
%{_libdir}/pkgconfig/glw.pc
%{_includedir}/GL/GLwDrawA.h
%{_includedir}/GL/GLwDrawAP.h
%{_includedir}/GL/GLwMDrawA.h
%{_includedir}/GL/GLwMDrawAP.h

%changelog
* Tue Nov 19 2019 Adam Jackson <ajax@redhat.com> - 8.0.0-18
- Update to git snapshot of the archived state

* Thu Jul 05 2018 Adam Jackson <ajax@redhat.com> - 8.0.0-14
- Drop useless %%defattr

* Fri Jun 29 2018 Adam Jackson <ajax@redhat.com> - 8.0.0-13
- Use ldconfig scriptlet macros

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 01 2015 Jon Ciesla <limburgher@gmail.com> - 8.0.0-7
- Move from lesstif to motif.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 10 2012 Adam Jackson <ajax@redhat.com> 8.0.0-1
- Switch to upstream's split-out glw release

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Bill Nottingham - 6.5.1-12
- fix prior macros

* Thu Jul 05 2012 Bill Nottingham - 6.5.1-11
- add conditional macros for openmotif/lesstif

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 6.5.1-6
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 6.5.1-5
- Autorebuild for GCC 4.3

* Fri Oct 12 2007 Matthias Clasen <mclasen@redhat.com> - 6.5.1-4
- Fix spec file syntax issues  (#330331)

* Tue Aug 21 2007 Adam Jackson <ajax@redhat.com> - 6.5.1-3
- Rebuild for build id

* Wed Jan 24 2007 Adam Jackson <ajax@redhat.com> 6.5.1-2
- Minor spec fixes (#210798)

* Fri Sep 29 2006 Adam Jackson <ajackson@redhat.com> 6.5.1-1
- lib64 fixes and cleanups from Patrice Dumas (#188974)

* Tue Sep 19 2006 Adam Jackson <ajackson@redhat.com> 6.5.1-0.2
- Use 6.5.1 release tarball.  Drop patches and build scripts that are no
  longer necessary.

* Tue Sep 19 2006 Adam Jackson <ajackson@redhat.com> 6.5.1-0.1
- Move revision back up to 6.5.1 for upgrade path from FC5.  Misc other
  spec fixes as per bug #188974 comment 30.

* Mon Sep 18 2006 Adam Jackson <ajackson@redhat.com> 1.0-4
- Rename back to mesa-libGLw as per bug #188974.

* Wed Aug 30 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.0-3
- Fix package for x86_64

* Tue Aug 29 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.0-2
- Fix package to depend on lesstif-devel
- -devel now Requires libGL-devel
- use name var in -devel Requires
- actually use RPM_OPT_FLAGS
- symlink devel libs, not copy (except for .*.*.*)

* Fri Aug  7 2006 Adam Jackson <ajackson@redhat.com> 1.0-1
- Split libGLw out from Mesa.
