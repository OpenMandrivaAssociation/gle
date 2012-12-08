%define major 3
%define libname %mklibname gle %{major}
%define develname %mklibname -d gle

Summary:	GLE Tubing and Extrusion Library
Name:		gle
Version:	3.1.0
Release:	15
License:	GPLv2
Group:		System/Libraries
Source:		gle-%{version}.tar.bz2
# (Anssi 05/2008) Link against libGL and libGLU to fix undefined symbols.
Patch0:		gle-3.1.0-link-with-gl+glu.patch
# (Anssi 05/2008) Fix Makefile.am files using += on unset CLEANFILES and SUFFIXES.
# This patch simply changes += to =, which AFAICS is correct here.
Patch1:		gle-3.1.0-fix-makefiles.patch
URL:		http://sourceforge.net/projects/gle
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xt)

%description
GLE is a library package of C functions that draw extruded surfaces,
including surfaces of revolution, sweeps, tubes, polycones,
polycylinders and helicoids.  Generically, the extruded surface is
specified with a 2D polyline that is extruded along a 3D path.  A
local coordinate system allows for additional flexibility in the
primitives drawn.  Extrusions may be texture mapped in a variety of
ways.  The GLE library generates 3D triangle coordinates, lighting
normal vectors and texture coordinates as output. GLE uses the GL or
OpenGL API's to perform the actual rendering.

%package -n %{libname}
Summary:	GLE shared library
Group:		System/Libraries

%description -n %{libname}
GLE is a library package of C functions that draw extruded surfaces,
including surfaces of revolution, sweeps, tubes, polycones,
polycylinders and helicoids.  Generically, the extruded surface is
specified with a 2D polyline that is extruded along a 3D path.  A
local coordinate system allows for additional flexibility in the
primitives drawn.  Extrusions may be texture mapped in a variety of
ways.  The GLE library generates 3D triangle coordinates, lighting
normal vectors and texture coordinates as output. GLE uses the GL or
OpenGL API's to perform the actual rendering.

The shared library needed by GLE applications.

%package -n %{develname}
Summary:	Devel files for GLE
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	libgle-devel = %{version}-%{release}
Provides:	gle-devel = %{version}-%{release}

%description -n %{develname}
GLE is a library package of C functions that draw extruded surfaces,
including surfaces of revolution, sweeps, tubes, polycones,
polycylinders and helicoids.  Generically, the extruded surface is
specified with a 2D polyline that is extruded along a 3D path.  A
local coordinate system allows for additional flexibility in the
primitives drawn.  Extrusions may be texture mapped in a variety of
ways.  The GLE library generates 3D triangle coordinates, lighting
normal vectors and texture coordinates as output. GLE uses the GL or
OpenGL API's to perform the actual rendering.

The static library and headers needed for developing GLE applications.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
find examples -name .cvsignore -exec rm {} \;

%build
# link-with-gl+glu.patch
autoreconf --force --install
%configure2_5x --disable-static
%make

%install
%makeinstall_std
mv %{buildroot}%{_datadir}/doc/gle installed-docs

cd examples
make clean

%files -n %{libname}
%doc README NEWS COPYING AUTHORS
%{_libdir}/libgle.so.%{major}*

%files -n %{develname}
%doc ChangeLog src/COPYING.src src/README.gutil examples installed-docs
%{_libdir}/libgle.so
%{_includedir}/GL/*
%{_mandir}/man3/*

%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 3.1.0-12mdv2011.0
+ Revision: 664850
- mass rebuild

* Wed Dec 22 2010 Funda Wang <fwang@mandriva.org> 3.1.0-11mdv2011.0
+ Revision: 623757
- tighten BR

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 3.1.0-10mdv2011.0
+ Revision: 605459
- rebuild

* Wed Jan 20 2010 GÃ¶tz Waschk <waschk@mandriva.org> 3.1.0-9mdv2010.1
+ Revision: 494020
- update license

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 3.1.0-8mdv2009.0
+ Revision: 264550
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri May 23 2008 Anssi Hannula <anssi@mandriva.org> 3.1.0-7mdv2009.0
+ Revision: 210591
- link against libGL and libGLU to fix undefined symbols
  (link-with-gl+glu.patch)
- fix makefiles regarding CLEANFILES and SUFFIXES (fix-makefiles.patch)
- ensure major correctness
- use configure2_5x

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 3.1.0-6mdv2008.1
+ Revision: 125768
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel


* Sun Jan 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 3.1.0-6mdv2007.0
+ Revision: 108692
- Import gle

* Sun Jan 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 3.1.0-6mdv2007.1
- Rebuild

* Mon May 22 2006 Götz Waschk <waschk@mandriva.org> 3.1.0-5mdk
- fix deps for Xorg 7
- use mkrel

* Sat May 21 2005 Götz Waschk <waschk@mandriva.org> 3.1.0-4mdk
- spec fixes

* Fri May 14 2004 Götz Waschk <waschk@linux-mandrake.com> 3.1.0-3mdk
- lib64 & deps fixes

