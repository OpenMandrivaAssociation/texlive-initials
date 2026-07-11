%global tl_name initials
%global tl_revision 54080

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Adobe Type 1 decorative initial fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/initials
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/initials.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/initials.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
For each font, at least a .pfb and a .tfm file is provided, with an .fd
file for use with LaTeX.

