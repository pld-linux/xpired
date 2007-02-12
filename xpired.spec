Summary:	Action-puzzle game
Summary(pl.UTF-8):   Gra zręcznościowo-logiczna
Name:		xpired
Version:	1.22
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/xpired/%{name}-%{version}-linux_source.tar.gz
# Source0-md5:	4d6e38efe53b3840beb38a8dc9cc72d1
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-Makefile.patch
URL:		http://xpired.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_gfx-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
The goal of the game in each level is to reach the exit square,
avoiding exploding barrels and other deadly stuff.

%description -l pl.UTF-8
Celem gry na każdym poziomie jest wyjść z kwadratu, unikając
eksplodujących beczek i innych zabójczych rzeczy.

%prep
%setup -q -c
%patch0 -p0

%build
%{__make} -C src \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},%{_sysconfdir}}

%{__make} -C src install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT


install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install src/xpired.cfg	$RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc src/readme.txt
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.cfg
%{_datadir}/%{name}
%{_pixmapsdir}/*
%{_desktopdir}/xpired.desktop
