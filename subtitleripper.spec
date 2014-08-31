Summary:	Command line tool to rip DVD subtitles
Name:		subtitleripper
Version:	0.3
Release:	8%{?dist}
License:	GPLv2+
Group:		Applications/Multimedia
URL:		http://subtitleripper.sourceforge.net/
Source0:	http://switch.dl.sourceforge.net/sourceforge/subtitleripper/%{name}-%{version}-4.tgz
Patch0:		pgm2txt.patch
Patch1:		Makefile.patch
Patch2:		binutils-gold.patch
BuildRequires:	netpbm-devel zlib-devel libpng-devel
Requires:	gocr transcode

%description
Converts DVD subtitles into text format (e.g. subrip format) or VobSub
format. Based on transcode.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .patch0
%patch1 -p1 -b .patch1
%patch2 -p1 -b .patch2

%build
CFLAGS="$RPM_OPT_FLAGS" make

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
for i in pgm2txt srttool subtitle2pgm subtitle2vobsub vobsub2pgm
do
  install -m 0755 $i $RPM_BUILD_ROOT/%{_bindir}
done

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/subtitleripper
install -m 644 *.sed $RPM_BUILD_ROOT%{_datadir}/subtitleripper

%files
%doc ChangeLog README*
%{_bindir}/pgm2txt
%{_bindir}/srttool
%{_bindir}/subtitle2pgm
%{_bindir}/subtitle2vobsub
%{_bindir}/vobsub2pgm
%{_datadir}/%{name}

%changelog
* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.3-7
- included and modified some patches from Debian/Ubuntu and Gentoo
- re-enable png support
- included .sed files for gocr
- included vobsub2pgm binary
- added requires on gocr and transcode
- cleanup spec to follow current Fedora guidelines

* Tue Aug 19 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.3-6
- added _default_patch_fuzz define

* Sun Aug 03 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.3-5
- rebuild

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field
- drop Epoch

* Wed Sep 21 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> 0:0.3-0.lvn.4
- Drop BR libpng, too

* Sat Sep 10 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> 0:0.3-0.lvn.3
- Disable png-support for now cause it does not compile on FC4

* Mon Jun 28 2004 Dams <anvil[AT]livna.org> 0:0.3-0.lvn.2.4
- BuildReq libpng-devel
- Fix for libnetpbm on FC2

* Mon Jun 28 2004 Dams <anvil[AT]livna.org> 0:0.3.4-0.lvn.1
- Updated to 0.3-4

* Wed May 14 2003 Dams <anvil[AT]livna.org> 0:0.3-0.fdr.2
- Added missing zlib-devel BuildRequires

* Sat May 10 2003 Dams <anvil[AT]livna.org> 
- Initial build.
