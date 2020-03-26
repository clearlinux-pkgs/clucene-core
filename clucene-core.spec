#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clucene-core
Version  : 2.3.3.4
Release  : 12
URL      : https://sourceforge.net/projects/clucene/files/clucene-core-unstable/2.3/clucene-core-2.3.3.4.tar.gz
Source0  : https://sourceforge.net/projects/clucene/files/clucene-core-unstable/2.3/clucene-core-2.3.3.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 LGPL-2.1
Requires: clucene-core-lib = %{version}-%{release}
Requires: clucene-core-license = %{version}-%{release}
BuildRequires : bash coreutils gzip
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : glibc-dev
BuildRequires : perl
BuildRequires : texlive
BuildRequires : zlib-dev
Patch1: clucene-core-2.3.3.4-install_contribs_lib.patch

%description
==============
------------------------------------------------------
CLucene is a C++ port of Lucene.
It is a high-performance, full-featured text search
engine written in C++. CLucene is faster than lucene
as it is written in C++.
------------------------------------------------------

%package dev
Summary: dev components for the clucene-core package.
Group: Development
Requires: clucene-core-lib = %{version}-%{release}
Provides: clucene-core-devel = %{version}-%{release}
Requires: clucene-core = %{version}-%{release}

%description dev
dev components for the clucene-core package.


%package lib
Summary: lib components for the clucene-core package.
Group: Libraries
Requires: clucene-core-license = %{version}-%{release}

%description lib
lib components for the clucene-core package.


%package license
Summary: license components for the clucene-core package.
Group: Default

%description license
license components for the clucene-core package.


%prep
%setup -q -n clucene-core-2.3.3.4
cd %{_builddir}/clucene-core-2.3.3.4
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585184631
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DBUILD_CONTRIBS=on -DBUILD_CONTRIBS_LIB=on
make  %{?_smp_mflags}  clucene-contribs-lib
popd

%install
export SOURCE_DATE_EPOCH=1585184631
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clucene-core
cp %{_builddir}/clucene-core-2.3.3.4/APACHE.license %{buildroot}/usr/share/package-licenses/clucene-core/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/clucene-core-2.3.3.4/COPYING %{buildroot}/usr/share/package-licenses/clucene-core/4570602f7785553392928a47e002ddccebaedad6
cp %{_builddir}/clucene-core-2.3.3.4/LGPL.license %{buildroot}/usr/share/package-licenses/clucene-core/1071adb104a2db491ae9db989a7ae8c31f5e3c7f
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/CLuceneConfig.cmake/CLuceneConfig.cmake

%files dev
%defattr(-,root,root,-)
/usr/include/CLucene.h
/usr/include/CLucene/CLConfig.h
/usr/include/CLucene/CLuceneConfig.cmake
/usr/include/CLucene/LuceneThreads.h
/usr/include/CLucene/SharedHeader.h
/usr/include/CLucene/StdHeader.h
/usr/include/CLucene/analysis/AnalysisHeader.h
/usr/include/CLucene/analysis/Analyzers.h
/usr/include/CLucene/analysis/CachingTokenFilter.h
/usr/include/CLucene/analysis/LanguageBasedAnalyzer.h
/usr/include/CLucene/analysis/PorterStemmer.h
/usr/include/CLucene/analysis/cjk/CJKAnalyzer.h
/usr/include/CLucene/analysis/de/GermanAnalyzer.h
/usr/include/CLucene/analysis/de/GermanStemFilter.h
/usr/include/CLucene/analysis/de/GermanStemmer.h
/usr/include/CLucene/analysis/standard/StandardAnalyzer.h
/usr/include/CLucene/analysis/standard/StandardFilter.h
/usr/include/CLucene/analysis/standard/StandardTokenizer.h
/usr/include/CLucene/analysis/standard/StandardTokenizerConstants.h
/usr/include/CLucene/clucene-config.h
/usr/include/CLucene/debug/error.h
/usr/include/CLucene/debug/lucenebase.h
/usr/include/CLucene/debug/mem.h
/usr/include/CLucene/document/DateField.h
/usr/include/CLucene/document/DateTools.h
/usr/include/CLucene/document/Document.h
/usr/include/CLucene/document/Field.h
/usr/include/CLucene/document/FieldSelector.h
/usr/include/CLucene/document/NumberTools.h
/usr/include/CLucene/ext/boost/assert.hpp
/usr/include/CLucene/ext/boost/checked_delete.hpp
/usr/include/CLucene/ext/boost/config.hpp
/usr/include/CLucene/ext/boost/config/abi/borland_prefix.hpp
/usr/include/CLucene/ext/boost/config/abi/borland_suffix.hpp
/usr/include/CLucene/ext/boost/config/abi/msvc_prefix.hpp
/usr/include/CLucene/ext/boost/config/abi/msvc_suffix.hpp
/usr/include/CLucene/ext/boost/config/abi_prefix.hpp
/usr/include/CLucene/ext/boost/config/abi_suffix.hpp
/usr/include/CLucene/ext/boost/config/auto_link.hpp
/usr/include/CLucene/ext/boost/config/compiler/borland.hpp
/usr/include/CLucene/ext/boost/config/compiler/codegear.hpp
/usr/include/CLucene/ext/boost/config/compiler/comeau.hpp
/usr/include/CLucene/ext/boost/config/compiler/common_edg.hpp
/usr/include/CLucene/ext/boost/config/compiler/compaq_cxx.hpp
/usr/include/CLucene/ext/boost/config/compiler/digitalmars.hpp
/usr/include/CLucene/ext/boost/config/compiler/gcc.hpp
/usr/include/CLucene/ext/boost/config/compiler/gcc_xml.hpp
/usr/include/CLucene/ext/boost/config/compiler/greenhills.hpp
/usr/include/CLucene/ext/boost/config/compiler/hp_acc.hpp
/usr/include/CLucene/ext/boost/config/compiler/intel.hpp
/usr/include/CLucene/ext/boost/config/compiler/kai.hpp
/usr/include/CLucene/ext/boost/config/compiler/metrowerks.hpp
/usr/include/CLucene/ext/boost/config/compiler/mpw.hpp
/usr/include/CLucene/ext/boost/config/compiler/pgi.hpp
/usr/include/CLucene/ext/boost/config/compiler/sgi_mipspro.hpp
/usr/include/CLucene/ext/boost/config/compiler/sunpro_cc.hpp
/usr/include/CLucene/ext/boost/config/compiler/vacpp.hpp
/usr/include/CLucene/ext/boost/config/compiler/visualc.hpp
/usr/include/CLucene/ext/boost/config/no_tr1/cmath.hpp
/usr/include/CLucene/ext/boost/config/no_tr1/complex.hpp
/usr/include/CLucene/ext/boost/config/no_tr1/functional.hpp
/usr/include/CLucene/ext/boost/config/no_tr1/memory.hpp
/usr/include/CLucene/ext/boost/config/no_tr1/utility.hpp
/usr/include/CLucene/ext/boost/config/platform/aix.hpp
/usr/include/CLucene/ext/boost/config/platform/amigaos.hpp
/usr/include/CLucene/ext/boost/config/platform/beos.hpp
/usr/include/CLucene/ext/boost/config/platform/bsd.hpp
/usr/include/CLucene/ext/boost/config/platform/cygwin.hpp
/usr/include/CLucene/ext/boost/config/platform/hpux.hpp
/usr/include/CLucene/ext/boost/config/platform/irix.hpp
/usr/include/CLucene/ext/boost/config/platform/linux.hpp
/usr/include/CLucene/ext/boost/config/platform/macos.hpp
/usr/include/CLucene/ext/boost/config/platform/qnxnto.hpp
/usr/include/CLucene/ext/boost/config/platform/solaris.hpp
/usr/include/CLucene/ext/boost/config/platform/vxworks.hpp
/usr/include/CLucene/ext/boost/config/platform/win32.hpp
/usr/include/CLucene/ext/boost/config/posix_features.hpp
/usr/include/CLucene/ext/boost/config/requires_threads.hpp
/usr/include/CLucene/ext/boost/config/select_compiler_config.hpp
/usr/include/CLucene/ext/boost/config/select_platform_config.hpp
/usr/include/CLucene/ext/boost/config/select_stdlib_config.hpp
/usr/include/CLucene/ext/boost/config/stdlib/dinkumware.hpp
/usr/include/CLucene/ext/boost/config/stdlib/libcomo.hpp
/usr/include/CLucene/ext/boost/config/stdlib/libstdcpp3.hpp
/usr/include/CLucene/ext/boost/config/stdlib/modena.hpp
/usr/include/CLucene/ext/boost/config/stdlib/msl.hpp
/usr/include/CLucene/ext/boost/config/stdlib/roguewave.hpp
/usr/include/CLucene/ext/boost/config/stdlib/sgi.hpp
/usr/include/CLucene/ext/boost/config/stdlib/stlport.hpp
/usr/include/CLucene/ext/boost/config/stdlib/vacpp.hpp
/usr/include/CLucene/ext/boost/config/suffix.hpp
/usr/include/CLucene/ext/boost/config/user.hpp
/usr/include/CLucene/ext/boost/config/warning_disable.hpp
/usr/include/CLucene/ext/boost/current_function.hpp
/usr/include/CLucene/ext/boost/detail/algorithm.hpp
/usr/include/CLucene/ext/boost/detail/allocator_utilities.hpp
/usr/include/CLucene/ext/boost/detail/atomic_count.hpp
/usr/include/CLucene/ext/boost/detail/binary_search.hpp
/usr/include/CLucene/ext/boost/detail/call_traits.hpp
/usr/include/CLucene/ext/boost/detail/catch_exceptions.hpp
/usr/include/CLucene/ext/boost/detail/compressed_pair.hpp
/usr/include/CLucene/ext/boost/detail/container_fwd.hpp
/usr/include/CLucene/ext/boost/detail/dynamic_bitset.hpp
/usr/include/CLucene/ext/boost/detail/endian.hpp
/usr/include/CLucene/ext/boost/detail/has_default_constructor.hpp
/usr/include/CLucene/ext/boost/detail/identifier.hpp
/usr/include/CLucene/ext/boost/detail/indirect_traits.hpp
/usr/include/CLucene/ext/boost/detail/interlocked.hpp
/usr/include/CLucene/ext/boost/detail/is_function_ref_tester.hpp
/usr/include/CLucene/ext/boost/detail/is_incrementable.hpp
/usr/include/CLucene/ext/boost/detail/is_xxx.hpp
/usr/include/CLucene/ext/boost/detail/iterator.hpp
/usr/include/CLucene/ext/boost/detail/lcast_precision.hpp
/usr/include/CLucene/ext/boost/detail/lightweight_mutex.hpp
/usr/include/CLucene/ext/boost/detail/lightweight_test.hpp
/usr/include/CLucene/ext/boost/detail/lightweight_thread.hpp
/usr/include/CLucene/ext/boost/detail/limits.hpp
/usr/include/CLucene/ext/boost/detail/named_template_params.hpp
/usr/include/CLucene/ext/boost/detail/no_exceptions_support.hpp
/usr/include/CLucene/ext/boost/detail/none_t.hpp
/usr/include/CLucene/ext/boost/detail/numeric_traits.hpp
/usr/include/CLucene/ext/boost/detail/ob_call_traits.hpp
/usr/include/CLucene/ext/boost/detail/ob_compressed_pair.hpp
/usr/include/CLucene/ext/boost/detail/quick_allocator.hpp
/usr/include/CLucene/ext/boost/detail/reference_content.hpp
/usr/include/CLucene/ext/boost/detail/scoped_enum_emulation.hpp
/usr/include/CLucene/ext/boost/detail/select_type.hpp
/usr/include/CLucene/ext/boost/detail/sp_typeinfo.hpp
/usr/include/CLucene/ext/boost/detail/templated_streams.hpp
/usr/include/CLucene/ext/boost/detail/utf8_codecvt_facet.hpp
/usr/include/CLucene/ext/boost/detail/workaround.hpp
/usr/include/CLucene/ext/boost/exception/all.hpp
/usr/include/CLucene/ext/boost/exception/current_exception_cast.hpp
/usr/include/CLucene/ext/boost/exception/detail/attribute_noreturn.hpp
/usr/include/CLucene/ext/boost/exception/detail/error_info_impl.hpp
/usr/include/CLucene/ext/boost/exception/detail/exception_ptr.hpp
/usr/include/CLucene/ext/boost/exception/detail/is_output_streamable.hpp
/usr/include/CLucene/ext/boost/exception/detail/object_hex_dump.hpp
/usr/include/CLucene/ext/boost/exception/detail/type_info.hpp
/usr/include/CLucene/ext/boost/exception/diagnostic_information.hpp
/usr/include/CLucene/ext/boost/exception/enable_current_exception.hpp
/usr/include/CLucene/ext/boost/exception/enable_error_info.hpp
/usr/include/CLucene/ext/boost/exception/errinfo_api_function.hpp
/usr/include/CLucene/ext/boost/exception/errinfo_at_line.hpp
/usr/include/CLucene/ext/boost/exception/errinfo_errno.hpp
/usr/include/CLucene/ext/boost/exception/errinfo_file_handle.hpp
/usr/include/CLucene/ext/boost/exception/errinfo_file_name.hpp
/usr/include/CLucene/ext/boost/exception/errinfo_file_open_mode.hpp
/usr/include/CLucene/ext/boost/exception/errinfo_nested_exception.hpp
/usr/include/CLucene/ext/boost/exception/errinfo_type_info_name.hpp
/usr/include/CLucene/ext/boost/exception/error_info.hpp
/usr/include/CLucene/ext/boost/exception/exception.hpp
/usr/include/CLucene/ext/boost/exception/get_error_info.hpp
/usr/include/CLucene/ext/boost/exception/info.hpp
/usr/include/CLucene/ext/boost/exception/info_tuple.hpp
/usr/include/CLucene/ext/boost/exception/to_string.hpp
/usr/include/CLucene/ext/boost/exception/to_string_stub.hpp
/usr/include/CLucene/ext/boost/memory_order.hpp
/usr/include/CLucene/ext/boost/shared_ptr.hpp
/usr/include/CLucene/ext/boost/smart_ptr/bad_weak_ptr.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/atomic_count.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/atomic_count_gcc.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/atomic_count_gcc_x86.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/atomic_count_pthreads.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/atomic_count_solaris.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/atomic_count_sync.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/atomic_count_win32.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/lightweight_mutex.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/lwm_nop.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/lwm_pthreads.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/lwm_win32_cs.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/operator_bool.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/quick_allocator.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/shared_array_nmt.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/shared_count.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/shared_ptr_nmt.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/sp_convertible.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/sp_counted_base.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/sp_counted_base_acc_ia64.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/sp_counted_base_cw_ppc.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/sp_counted_base_cw_x86.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/sp_counted_base_gcc_ia64.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/sp_counted_base_gcc_mips.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/sp_counted_base_gcc_ppc.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/sp_counted_base_gcc_sparc.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/sp_counted_base_gcc_x86.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/sp_counted_base_nt.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/sp_counted_base_pt.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/sp_counted_base_solaris.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/sp_counted_base_spin.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/sp_counted_base_sync.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/sp_counted_base_w32.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/sp_counted_impl.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/sp_has_sync.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/spinlock.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/spinlock_gcc_arm.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/spinlock_nt.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/spinlock_pool.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/spinlock_pt.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/spinlock_sync.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/spinlock_w32.hpp
/usr/include/CLucene/ext/boost/smart_ptr/detail/yield_k.hpp
/usr/include/CLucene/ext/boost/smart_ptr/enable_shared_from_this.hpp
/usr/include/CLucene/ext/boost/smart_ptr/enable_shared_from_this2.hpp
/usr/include/CLucene/ext/boost/smart_ptr/intrusive_ptr.hpp
/usr/include/CLucene/ext/boost/smart_ptr/make_shared.hpp
/usr/include/CLucene/ext/boost/smart_ptr/scoped_array.hpp
/usr/include/CLucene/ext/boost/smart_ptr/scoped_ptr.hpp
/usr/include/CLucene/ext/boost/smart_ptr/shared_array.hpp
/usr/include/CLucene/ext/boost/smart_ptr/shared_ptr.hpp
/usr/include/CLucene/ext/boost/smart_ptr/weak_ptr.hpp
/usr/include/CLucene/ext/boost/throw_exception.hpp
/usr/include/CLucene/ext/boost/version.hpp
/usr/include/CLucene/highlighter/Encoder.h
/usr/include/CLucene/highlighter/Formatter.h
/usr/include/CLucene/highlighter/Fragmenter.h
/usr/include/CLucene/highlighter/HighlightScorer.h
/usr/include/CLucene/highlighter/Highlighter.h
/usr/include/CLucene/highlighter/QueryScorer.h
/usr/include/CLucene/highlighter/QueryTermExtractor.h
/usr/include/CLucene/highlighter/Scorer.h
/usr/include/CLucene/highlighter/SimpleFragmenter.h
/usr/include/CLucene/highlighter/SimpleHTMLEncoder.h
/usr/include/CLucene/highlighter/SimpleHTMLFormatter.h
/usr/include/CLucene/highlighter/TextFragment.h
/usr/include/CLucene/highlighter/TokenGroup.h
/usr/include/CLucene/highlighter/TokenSources.h
/usr/include/CLucene/highlighter/WeightedTerm.h
/usr/include/CLucene/index/DirectoryIndexReader.h
/usr/include/CLucene/index/IndexDeletionPolicy.h
/usr/include/CLucene/index/IndexModifier.h
/usr/include/CLucene/index/IndexReader.h
/usr/include/CLucene/index/IndexWriter.h
/usr/include/CLucene/index/MergePolicy.h
/usr/include/CLucene/index/MergeScheduler.h
/usr/include/CLucene/index/MultiReader.h
/usr/include/CLucene/index/MultipleTermPositions.h
/usr/include/CLucene/index/Payload.h
/usr/include/CLucene/index/Term.h
/usr/include/CLucene/index/TermVector.h
/usr/include/CLucene/index/Terms.h
/usr/include/CLucene/queryParser/MultiFieldQueryParser.h
/usr/include/CLucene/queryParser/QueryParser.h
/usr/include/CLucene/queryParser/QueryParserConstants.h
/usr/include/CLucene/queryParser/QueryParserTokenManager.h
/usr/include/CLucene/queryParser/QueryToken.h
/usr/include/CLucene/queryParser/legacy/MultiFieldQueryParser.h
/usr/include/CLucene/queryParser/legacy/QueryParser.h
/usr/include/CLucene/queryParser/legacy/QueryToken.h
/usr/include/CLucene/search/BooleanClause.h
/usr/include/CLucene/search/BooleanQuery.h
/usr/include/CLucene/search/CachingSpanFilter.h
/usr/include/CLucene/search/CachingWrapperFilter.h
/usr/include/CLucene/search/ChainedFilter.h
/usr/include/CLucene/search/Compare.h
/usr/include/CLucene/search/ConstantScoreQuery.h
/usr/include/CLucene/search/DateFilter.h
/usr/include/CLucene/search/Explanation.h
/usr/include/CLucene/search/FieldCache.h
/usr/include/CLucene/search/FieldDoc.h
/usr/include/CLucene/search/FieldSortedHitQueue.h
/usr/include/CLucene/search/Filter.h
/usr/include/CLucene/search/FilterResultCache.h
/usr/include/CLucene/search/FilteredTermEnum.h
/usr/include/CLucene/search/FuzzyQuery.h
/usr/include/CLucene/search/Hits.h
/usr/include/CLucene/search/IndexSearcher.h
/usr/include/CLucene/search/MatchAllDocsQuery.h
/usr/include/CLucene/search/MultiPhraseQuery.h
/usr/include/CLucene/search/MultiSearcher.h
/usr/include/CLucene/search/MultiTermQuery.h
/usr/include/CLucene/search/PhraseQuery.h
/usr/include/CLucene/search/PrefixQuery.h
/usr/include/CLucene/search/Query.h
/usr/include/CLucene/search/QueryFilter.h
/usr/include/CLucene/search/RangeFilter.h
/usr/include/CLucene/search/RangeQuery.h
/usr/include/CLucene/search/Scorer.h
/usr/include/CLucene/search/ScorerDocQueue.h
/usr/include/CLucene/search/SearchHeader.h
/usr/include/CLucene/search/Searchable.h
/usr/include/CLucene/search/Similarity.h
/usr/include/CLucene/search/Sort.h
/usr/include/CLucene/search/SpanFilter.h
/usr/include/CLucene/search/SpanFilterResult.h
/usr/include/CLucene/search/SpanQueryFilter.h
/usr/include/CLucene/search/TermQuery.h
/usr/include/CLucene/search/WildcardQuery.h
/usr/include/CLucene/search/WildcardTermEnum.h
/usr/include/CLucene/search/spans/SpanFirstQuery.h
/usr/include/CLucene/search/spans/SpanNearQuery.h
/usr/include/CLucene/search/spans/SpanNotQuery.h
/usr/include/CLucene/search/spans/SpanOrQuery.h
/usr/include/CLucene/search/spans/SpanQuery.h
/usr/include/CLucene/search/spans/SpanScorer.h
/usr/include/CLucene/search/spans/SpanTermQuery.h
/usr/include/CLucene/search/spans/SpanWeight.h
/usr/include/CLucene/search/spans/Spans.h
/usr/include/CLucene/snowball/SnowballAnalyzer.h
/usr/include/CLucene/snowball/SnowballFilter.h
/usr/include/CLucene/snowball/include/libstemmer.h
/usr/include/CLucene/snowball/libstemmer.h
/usr/include/CLucene/snowball/libstemmer/modules.h
/usr/include/CLucene/snowball/runtime/api.h
/usr/include/CLucene/snowball/runtime/header.h
/usr/include/CLucene/snowball/src_c/stem_ISO_8859_1_danish.h
/usr/include/CLucene/snowball/src_c/stem_ISO_8859_1_dutch.h
/usr/include/CLucene/snowball/src_c/stem_ISO_8859_1_english.h
/usr/include/CLucene/snowball/src_c/stem_ISO_8859_1_finnish.h
/usr/include/CLucene/snowball/src_c/stem_ISO_8859_1_french.h
/usr/include/CLucene/snowball/src_c/stem_ISO_8859_1_german.h
/usr/include/CLucene/snowball/src_c/stem_ISO_8859_1_italian.h
/usr/include/CLucene/snowball/src_c/stem_ISO_8859_1_norwegian.h
/usr/include/CLucene/snowball/src_c/stem_ISO_8859_1_porter.h
/usr/include/CLucene/snowball/src_c/stem_ISO_8859_1_portuguese.h
/usr/include/CLucene/snowball/src_c/stem_ISO_8859_1_spanish.h
/usr/include/CLucene/snowball/src_c/stem_ISO_8859_1_swedish.h
/usr/include/CLucene/snowball/src_c/stem_KOI8_R_russian.h
/usr/include/CLucene/snowball/src_c/stem_UTF_8_danish.h
/usr/include/CLucene/snowball/src_c/stem_UTF_8_dutch.h
/usr/include/CLucene/snowball/src_c/stem_UTF_8_english.h
/usr/include/CLucene/snowball/src_c/stem_UTF_8_finnish.h
/usr/include/CLucene/snowball/src_c/stem_UTF_8_french.h
/usr/include/CLucene/snowball/src_c/stem_UTF_8_german.h
/usr/include/CLucene/snowball/src_c/stem_UTF_8_italian.h
/usr/include/CLucene/snowball/src_c/stem_UTF_8_norwegian.h
/usr/include/CLucene/snowball/src_c/stem_UTF_8_porter.h
/usr/include/CLucene/snowball/src_c/stem_UTF_8_portuguese.h
/usr/include/CLucene/snowball/src_c/stem_UTF_8_russian.h
/usr/include/CLucene/snowball/src_c/stem_UTF_8_spanish.h
/usr/include/CLucene/snowball/src_c/stem_UTF_8_swedish.h
/usr/include/CLucene/store/Directory.h
/usr/include/CLucene/store/FSDirectory.h
/usr/include/CLucene/store/IndexInput.h
/usr/include/CLucene/store/IndexOutput.h
/usr/include/CLucene/store/Lock.h
/usr/include/CLucene/store/LockFactory.h
/usr/include/CLucene/store/RAMDirectory.h
/usr/include/CLucene/util/Array.h
/usr/include/CLucene/util/BitSet.h
/usr/include/CLucene/util/CLStreams.h
/usr/include/CLucene/util/Equators.h
/usr/include/CLucene/util/PriorityQueue.h
/usr/include/CLucene/util/Reader.h
/usr/include/CLucene/util/VoidList.h
/usr/include/CLucene/util/VoidMap.h
/usr/include/CLucene/util/arrayinputstream.h
/usr/include/CLucene/util/byteinputstream.h
/usr/include/CLucene/util/gzipcompressstream.h
/usr/include/CLucene/util/gzipinputstream.h
/usr/include/CLucene/util/streamarray.h
/usr/lib64/libclucene-contribs-lib.so
/usr/lib64/libclucene-core.so
/usr/lib64/libclucene-shared.so
/usr/lib64/pkgconfig/libclucene-core.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libclucene-contribs-lib.so.1
/usr/lib64/libclucene-contribs-lib.so.2.3.3.4
/usr/lib64/libclucene-core.so.1
/usr/lib64/libclucene-core.so.2.3.3.4
/usr/lib64/libclucene-shared.so.1
/usr/lib64/libclucene-shared.so.2.3.3.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clucene-core/1071adb104a2db491ae9db989a7ae8c31f5e3c7f
/usr/share/package-licenses/clucene-core/4570602f7785553392928a47e002ddccebaedad6
/usr/share/package-licenses/clucene-core/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
