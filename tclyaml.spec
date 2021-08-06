%define buildroot %{_tmppath}/%{name}

Name:          tclyaml
Summary:       Tcl binding to libyaml 
Version:       0.5
Release:       0
License:       TCL
Group:         Development/Libraries/Tcl
Source:        %{name}-%{version}.tar.gz
URL:           https://github.com/andreas-kupries/tclyaml
BuildRequires: gcc
BuildRequires: tcl >= 8.5
BuildRequires: tcl-kettle
BuildRequires: critcl
BuildRequires: critcl-devel
BuildRequires: tcllib
Requires:      tcl >= 8.5
Requires:      critcl
Requires:      critcl-devel
BuildRoot:     %{buildroot}

%description
TclYAML is a binding to the C-based libyaml parser library.

%prep
%setup -q -n %{name}-%{version}

%build

%install
tclsh /usr/bin/kettle -f build.tcl --lib-dir %{buildroot}%_libdir/tcl \
--include-dir %{buildroot}/usr/include install-package-tclyaml

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{tcl_archdir}

