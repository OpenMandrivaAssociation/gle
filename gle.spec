%define major	3
%define libname %mklibname gle %{major}
%define devname %mklibname -d gle

Summary:	GLE Tubing and Extrusion Library
Name:		gle
Version:	3.1.0
Release:	19
License:	GPLv2
Group:		System/Libraries
Url:		http://sourceforge.net/projects/gle
Source0:	gle-%{version}.tar.bz2
# (Anssi 05/2008) Link against libGL and libGLU to fix undefined symbols.
Patch0:		gle-3.1.0-link-with-gl+glu.patch
# (Anssi 05/2008) Fix Makefile.am files using += on unset CLEANFILES and SUFFIXES.
# This patch simply changes += to =, which AFAICS is correct here.
Patch1:		gle-3.1.0-fix-makefiles.patch
Patch2:		gle-3.1.0-automake-1.13.patch

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

%package -n %{devname}
Summary:	Devel files for GLE
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
The development library and headers needed for developing GLE applications.

%prep
%setup -q
%apply_patches
find examples -name .cvsignore -exec rm {} \;

# link-with-gl+glu.patch
autoreconf -fi

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std
mv %{buildroot}%{_datadir}/doc/gle installed-docs

cd examples
make clean

%files -n %{libname}
%{_libdir}/libgle.so.%{major}*

%files -n %{devname}
%doc README NEWS COPYING AUTHORS
%doc ChangeLog src/COPYING.src src/README.gutil examples installed-docs
%{_libdir}/libgle.so
%{_includedir}/GL/*
%{_mandir}/man3/*

