%define name heap-buddy
%define version 0.2
%define release %mkrel 4
%define libname %mklibname %name 0
Summary: Heap profiler for mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://go-mono.com/sources/heap-buddy/%{name}-%{version}.tar.bz2
Patch0: heap-buddy-0.2-fix-build.patch
License: MIT
Group: Development/Other
Url: https://www.mono-project.com/Main_Page
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
Requires: %libname = %version

%description
Heap-buddy is a heap profiler for mono.  It attaches to special hooks in the
mono runtime and tracks all of the managed memory allocations, every garbage
collection and every heap resize.  These statistics are written out into a
data file that we call an 'outfile'.

%package -n %libname
Summary: Heap profiler for mono library
Group: System/Libraries

%description -n %libname
Heap-buddy is a heap profiler for mono.  It attaches to special hooks in the
mono runtime and tracks all of the managed memory allocations, every garbage
collection and every heap resize.  These statistics are written out into a
data file that we call an 'outfile'.


%prep
%setup -q
%autopatch -p1

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/lib*.so
rm -f %buildroot%_libdir/lib*a

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc README NEWS AUTHORS
%_bindir/%name
%_libdir/%name

%files -n %libname
%defattr(-,root,root)
%_libdir/libmono-profiler-heap-buddy.so.*


