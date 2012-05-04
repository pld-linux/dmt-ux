Summary:	DMT-UX - DSL Modem Tool for Unix
Name:		dmt-ux
Version:	0.178
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://www.spida.net/projects/software/dmt-ux/%{name}-%{version}.tgz
# Source0-md5:	fe496f30f777661a14e2d12a257c964e
URL:		http://www.spida.net/projects/software/dmt-ux/index.en.html
BuildRequires:	freetype-devel
BuildRequires:	libpng-devel
BuildRequires:	rrdtool
Requires:	fonts-TTF-bitstream-vera
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DSL Modem Tool, as written by A. Matthoefer, is a very usefull tool
for diagnosing and tuning of dsl-modems. Sadly it is written for
Windows only, so I have started to reimplement it for Linux.

DMT-UX should be able to communicate with Thomson Speedtouch and all
compatible modems.

Features:
- DMT-UX reads technical information about the modem
- DMT-UX can show a graphical analysis of the line-quality logging of
  changes of the line-quality and synchronisation

%prep
%setup -q

%{__sed} -i -e 's:./fonts/Vera.ttf:/usr/share/fonts/TTF/Vera.ttf:' dmt-ux.c

%build
CFLAGS="%{rpmcflags}" \
%{__make} \
	CC="%{__cc}" \
	_LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p dmt-ux $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/README
%attr(755,root,root) %{_bindir}/dmt-ux
