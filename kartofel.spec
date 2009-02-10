Summary:	The game of skill and logic
Summary(pl.UTF-8):	Gra zręcznościowo-logiczna
Name:		kartofel
Version:	1.2
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://kartofel.jfedor.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	4452da69e2e5c8f78ac22e234594dabf
Source1:	%{name}.desktop
Patch0:		%{name}-link.patch
Patch1:		%{name}-config.patch
URL:		http://kartofel.jfedor.org/
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	curl-devel
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kartofel is a game of skill and logic. The objective is to connect the
numbered dots in order, without crossing over yourself.

%description -l pl.UTF-8
Kartofel jest grą zręcznościowo-logiczną. Zadaniem gracza jest
łączenie ponumerowanych kropek w odpowiedniej kolejności, nie
przecinając istniejących już połączeń.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%{__sed} -i 's@g++@$(CXX)@' Makefile

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXOPTIONS="%{rpmcxxflags} `sdl-config --cflags` `curl-config --cflags`" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_desktopdir},%{_pixmapsdir}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

install images/icon32x32.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
install kartofel $RPM_BUILD_ROOT%{_bindir}
install kartofel.txt $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -r {fonts,images,levels,music,sounds} $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES COPYRIGHT README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
