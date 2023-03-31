Name:		texlive-initials
Version:	54080
Release:	2
Summary:	Adobe Type 1 decorative initial fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/initials
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/initials.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/initials.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex

%description
For each font, at least an .pfb and .tfm file is provided, with
a .fd file for use with LaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/initials/config.Acorn
%{_texmfdistdir}/dvips/initials/config.AnnSton
%{_texmfdistdir}/dvips/initials/config.ArtNouv
%{_texmfdistdir}/dvips/initials/config.ArtNouvc
%{_texmfdistdir}/dvips/initials/config.Carrickc
%{_texmfdistdir}/dvips/initials/config.Eichenla
%{_texmfdistdir}/dvips/initials/config.Eileen
%{_texmfdistdir}/dvips/initials/config.EileenBl
%{_texmfdistdir}/dvips/initials/config.Elzevier
%{_texmfdistdir}/dvips/initials/config.GotIn
%{_texmfdistdir}/dvips/initials/config.GoudyIn
%{_texmfdistdir}/dvips/initials/config.Kinigcap
%{_texmfdistdir}/dvips/initials/config.Konanur
%{_texmfdistdir}/dvips/initials/config.Kramer
%{_texmfdistdir}/dvips/initials/config.MorrisIn
%{_texmfdistdir}/dvips/initials/config.Nouveaud
%{_texmfdistdir}/dvips/initials/config.Romantik
%{_texmfdistdir}/dvips/initials/config.Rothdn
%{_texmfdistdir}/dvips/initials/config.RoyalIn
%{_texmfdistdir}/dvips/initials/config.Sanremo
%{_texmfdistdir}/dvips/initials/config.Starburst
%{_texmfdistdir}/dvips/initials/config.Typocaps
%{_texmfdistdir}/dvips/initials/config.Zallman
%{_texmfdistdir}/fonts/afm/public/initials/Acorn.afm
%{_texmfdistdir}/fonts/afm/public/initials/AnnSton.afm
%{_texmfdistdir}/fonts/afm/public/initials/ArtNouv.afm
%{_texmfdistdir}/fonts/afm/public/initials/ArtNouvc.afm
%{_texmfdistdir}/fonts/afm/public/initials/Carrickc.afm
%{_texmfdistdir}/fonts/afm/public/initials/Eichenla.afm
%{_texmfdistdir}/fonts/afm/public/initials/Eileen.afm
%{_texmfdistdir}/fonts/afm/public/initials/EileenBl.afm
%{_texmfdistdir}/fonts/afm/public/initials/Elzevier.afm
%{_texmfdistdir}/fonts/afm/public/initials/GotIn.afm
%{_texmfdistdir}/fonts/afm/public/initials/GoudyIn.afm
%{_texmfdistdir}/fonts/afm/public/initials/Kinigcap.afm
%{_texmfdistdir}/fonts/afm/public/initials/Konanur.afm
%{_texmfdistdir}/fonts/afm/public/initials/Kramer.afm
%{_texmfdistdir}/fonts/afm/public/initials/MorrisIn.afm
%{_texmfdistdir}/fonts/afm/public/initials/Nouveaud.afm
%{_texmfdistdir}/fonts/afm/public/initials/Romantik.afm
%{_texmfdistdir}/fonts/afm/public/initials/Rothdn.afm
%{_texmfdistdir}/fonts/afm/public/initials/RoyalIn.afm
%{_texmfdistdir}/fonts/afm/public/initials/Sanremo.afm
%{_texmfdistdir}/fonts/afm/public/initials/Starburst.afm
%{_texmfdistdir}/fonts/afm/public/initials/Typocaps.afm
%{_texmfdistdir}/fonts/afm/public/initials/Zallman.afm
%{_texmfdistdir}/fonts/map/dvips/initials/Acorn.map
%{_texmfdistdir}/fonts/map/dvips/initials/AnnSton.map
%{_texmfdistdir}/fonts/map/dvips/initials/ArtNouv.map
%{_texmfdistdir}/fonts/map/dvips/initials/ArtNouvc.map
%{_texmfdistdir}/fonts/map/dvips/initials/Carrickc.map
%{_texmfdistdir}/fonts/map/dvips/initials/Eichenla.map
%{_texmfdistdir}/fonts/map/dvips/initials/Eileen.map
%{_texmfdistdir}/fonts/map/dvips/initials/EileenBl.map
%{_texmfdistdir}/fonts/map/dvips/initials/Elzevier.map
%{_texmfdistdir}/fonts/map/dvips/initials/GotIn.map
%{_texmfdistdir}/fonts/map/dvips/initials/GoudyIn.map
%{_texmfdistdir}/fonts/map/dvips/initials/Kinigcap.map
%{_texmfdistdir}/fonts/map/dvips/initials/Konanur.map
%{_texmfdistdir}/fonts/map/dvips/initials/Kramer.map
%{_texmfdistdir}/fonts/map/dvips/initials/MorrisIn.map
%{_texmfdistdir}/fonts/map/dvips/initials/Nouveaud.map
%{_texmfdistdir}/fonts/map/dvips/initials/Romantik.map
%{_texmfdistdir}/fonts/map/dvips/initials/Rothdn.map
%{_texmfdistdir}/fonts/map/dvips/initials/RoyalIn.map
%{_texmfdistdir}/fonts/map/dvips/initials/Sanremo.map
%{_texmfdistdir}/fonts/map/dvips/initials/Starburst.map
%{_texmfdistdir}/fonts/map/dvips/initials/Typocaps.map
%{_texmfdistdir}/fonts/map/dvips/initials/Zallman.map
%{_texmfdistdir}/fonts/tfm/public/initials/Acorn.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/AnnSton.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/ArtNouv.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/ArtNouvc.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Carrickc.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Eichenla.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Eileen.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/EileenBl.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Elzevier.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/GotIn.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/GoudyIn.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Kinigcap.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Konanur.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Kramer.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/MorrisIn.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Nouveaud.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Romantik.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Rothdn.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/RoyalIn.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Sanremo.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Starburst.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Typocaps.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Zallman.tfm
%{_texmfdistdir}/fonts/type1/public/initials/Acorn.pfb
%{_texmfdistdir}/fonts/type1/public/initials/AnnSton.pfb
%{_texmfdistdir}/fonts/type1/public/initials/ArtNouv.pfb
%{_texmfdistdir}/fonts/type1/public/initials/ArtNouvc.pfb
%{_texmfdistdir}/fonts/type1/public/initials/Carrickc.pfb
%{_texmfdistdir}/fonts/type1/public/initials/Eichenla.pfb
%{_texmfdistdir}/fonts/type1/public/initials/Eileen.pfb
%{_texmfdistdir}/fonts/type1/public/initials/EileenBl.pfb
%{_texmfdistdir}/fonts/type1/public/initials/Elzevier.pfb
%{_texmfdistdir}/fonts/type1/public/initials/GotIn.pfb
%{_texmfdistdir}/fonts/type1/public/initials/GoudyIn.pfb
%{_texmfdistdir}/fonts/type1/public/initials/Kinigcap.pfb
%{_texmfdistdir}/fonts/type1/public/initials/Konanur.pfb
%{_texmfdistdir}/fonts/type1/public/initials/Kramer.pfb
%{_texmfdistdir}/fonts/type1/public/initials/MorrisIn.pfb
%{_texmfdistdir}/fonts/type1/public/initials/Nouveaud.pfb
%{_texmfdistdir}/fonts/type1/public/initials/Romantik.pfb
%{_texmfdistdir}/fonts/type1/public/initials/Rothdn.pfb
%{_texmfdistdir}/fonts/type1/public/initials/RoyalIn.pfb
%{_texmfdistdir}/fonts/type1/public/initials/Sanremo.pfb
%{_texmfdistdir}/fonts/type1/public/initials/Starburst.pfb
%{_texmfdistdir}/fonts/type1/public/initials/Typocaps.pfb
%{_texmfdistdir}/fonts/type1/public/initials/Zallman.pfb
%{_texmfdistdir}/tex/latex/initials/Acorn.fd
%{_texmfdistdir}/tex/latex/initials/AnnSton.fd
%{_texmfdistdir}/tex/latex/initials/ArtNouv.fd
%{_texmfdistdir}/tex/latex/initials/ArtNouvc.fd
%{_texmfdistdir}/tex/latex/initials/Carrickc.fd
%{_texmfdistdir}/tex/latex/initials/Eichenla.fd
%{_texmfdistdir}/tex/latex/initials/Eileen.fd
%{_texmfdistdir}/tex/latex/initials/EileenBl.fd
%{_texmfdistdir}/tex/latex/initials/Elzevier.fd
%{_texmfdistdir}/tex/latex/initials/GotIn.fd
%{_texmfdistdir}/tex/latex/initials/GoudyIn.fd
%{_texmfdistdir}/tex/latex/initials/Kinigcap.fd
%{_texmfdistdir}/tex/latex/initials/Konanur.fd
%{_texmfdistdir}/tex/latex/initials/Kramer.fd
%{_texmfdistdir}/tex/latex/initials/MorrisIn.fd
%{_texmfdistdir}/tex/latex/initials/Nouveaud.fd
%{_texmfdistdir}/tex/latex/initials/Romantik.fd
%{_texmfdistdir}/tex/latex/initials/Rothdn.fd
%{_texmfdistdir}/tex/latex/initials/RoyalIn.fd
%{_texmfdistdir}/tex/latex/initials/Sanremo.fd
%{_texmfdistdir}/tex/latex/initials/Starburst.fd
%{_texmfdistdir}/tex/latex/initials/Typocaps.fd
%{_texmfdistdir}/tex/latex/initials/Zallman.fd
%_texmf_updmap_d/initials
%doc %{_texmfdistdir}/doc/fonts/initials/Acorn.tex
%doc %{_texmfdistdir}/doc/fonts/initials/AnnSton.tex
%doc %{_texmfdistdir}/doc/fonts/initials/ArtNouv.tex
%doc %{_texmfdistdir}/doc/fonts/initials/ArtNouvc.tex
%doc %{_texmfdistdir}/doc/fonts/initials/Carrickc.tex
%doc %{_texmfdistdir}/doc/fonts/initials/Eichenla.tex
%doc %{_texmfdistdir}/doc/fonts/initials/Eileen.tex
%doc %{_texmfdistdir}/doc/fonts/initials/EileenBl.tex
%doc %{_texmfdistdir}/doc/fonts/initials/Elzevier.tex
%doc %{_texmfdistdir}/doc/fonts/initials/GotIn.tex
%doc %{_texmfdistdir}/doc/fonts/initials/GoudyIn.tex
%doc %{_texmfdistdir}/doc/fonts/initials/Kinigcap.tex
%doc %{_texmfdistdir}/doc/fonts/initials/Konanur.tex
%doc %{_texmfdistdir}/doc/fonts/initials/Kramer.tex
%doc %{_texmfdistdir}/doc/fonts/initials/MorrisIn.tex
%doc %{_texmfdistdir}/doc/fonts/initials/Nouveaud.tex
%doc %{_texmfdistdir}/doc/fonts/initials/README
%doc %{_texmfdistdir}/doc/fonts/initials/Romantik.tex
%doc %{_texmfdistdir}/doc/fonts/initials/Rothdn.tex
%doc %{_texmfdistdir}/doc/fonts/initials/RoyalIn.tex
%doc %{_texmfdistdir}/doc/fonts/initials/Sanremo.tex
%doc %{_texmfdistdir}/doc/fonts/initials/Starburst.tex
%doc %{_texmfdistdir}/doc/fonts/initials/Typocaps.tex
%doc %{_texmfdistdir}/doc/fonts/initials/Zallman.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/initials <<EOF
Map Acorn.map
Map AnnSton.map
Map ArtNouv.map
Map ArtNouvc.map
Map Carrickc.map
Map Eichenla.map
Map Eileen.map
Map EileenBl.map
Map Elzevier.map
Map GotIn.map
Map GoudyIn.map
Map Kinigcap.map
Map Konanur.map
Map Kramer.map
Map MorrisIn.map
Map Nouveaud.map
Map Romantik.map
Map Rothdn.map
Map RoyalIn.map
Map Sanremo.map
Map Starburst.map
Map Typocaps.map
Map Zallman.map
EOF
