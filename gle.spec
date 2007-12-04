%define major 3
%define libname %mklibname gle %major

Summary:  GLE Tubing and Extrusion Library
Name: gle
Version: 3.1.0
Release: %mkrel 6
License: GPL
Group: System/Libraries
Source: gle-%{version}.tar.bz2
URL: http://sourceforge.net/projects/gle
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: libmesaglu-devel >= 4.0.1
BuildRequires: libmesaglut-devel >= 4.0.1
BuildRequires: X11-devel

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

%package -n %libname
Summary:     	GLE shared library
Group: 		System/Libraries

%description -n %libname
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

%package -n %libname-devel
Summary:        Devel files for GLE
Group:          Development/C
Requires:	%libname = %version
Provides:	libgle-devel = %version
Provides:	gle-devel = %version
%description -n %libname-devel
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
find examples -name .cvsignore -exec rm {} \;

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT installed-docs
%makeinstall_std
mv %buildroot%_datadir/doc/gle installed-docs

cd examples
make clean

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-, root, root)
%doc README NEWS COPYING AUTHORS
%_libdir/libgle.so.*

%files -n %libname-devel
%defattr(-, root, root)
%doc ChangeLog src/COPYING.src src/README.gutil examples installed-docs
%_libdir/libgle.so
%_libdir/libgle.la
%_libdir/libgle.a
%_includedir/GL/*
%_mandir/man3/*


