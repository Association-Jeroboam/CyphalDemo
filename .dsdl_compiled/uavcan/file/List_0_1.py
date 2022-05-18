# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/file/406.List.0.1.dsdl
#
# Generated at:  2022-05-18 08:39:25.814218 UTC
# Is deprecated: yes
# Fixed port ID: 406
# Full name:     uavcan.file.List
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import warnings as _warnings_
import uavcan.file


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class List_0_1:
    # noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
    class Request:
        """
        Generated property settings use relaxed type signatures, accepting a large variety of
        possible representations of the value, which are automatically converted to a well-defined
        internal representation. When accessing a property, this strict well-defined internal
        representation is always returned. The implicit strictification enables more precise static
        type analysis.

        The value returned by the __repr__() method may be invariant to some of the field values,
        and its format is not guaranteed to be stable. Therefore, the returned string representation
        can be used only for displaying purposes; any kind of automation build on top of that will
        be fragile and prone to mismaintenance.
        """
        def __init__(self,
                     entry_index:    None | int | _np_.uint32 = None,
                     directory_path: None | uavcan.file.Path_1_0 = None) -> None:
            """
            uavcan.file.List.Request.0.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param entry_index:    saturated uint32 entry_index
            :param directory_path: uavcan.file.Path.1.0 directory_path
            """
            _warnings_.warn('Data type uavcan.file.List.Request.0.1 is deprecated', DeprecationWarning)

            self._entry_index:    int
            self._directory_path: uavcan.file.Path_1_0

            self.entry_index = entry_index if entry_index is not None else 0  # type: ignore

            if directory_path is None:
                self.directory_path = uavcan.file.Path_1_0()
            elif isinstance(directory_path, uavcan.file.Path_1_0):
                self.directory_path = directory_path
            else:
                raise ValueError(f'directory_path: expected uavcan.file.Path_1_0 '
                                 f'got {type(directory_path).__name__}')

        @property
        def entry_index(self) -> int:
            """
            saturated uint32 entry_index
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._entry_index

        @entry_index.setter
        def entry_index(self, x: int | _np_.uint32) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 4294967295:
                self._entry_index = x
            else:
                raise ValueError(f'entry_index: value {x} is not in [0, 4294967295]')

        @property
        def directory_path(self) -> uavcan.file.Path_1_0:
            """
            uavcan.file.Path.1.0 directory_path
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._directory_path

        @directory_path.setter
        def directory_path(self, x: uavcan.file.Path_1_0) -> None:
            if isinstance(x, uavcan.file.Path_1_0):
                self._directory_path = x
            else:
                raise ValueError(f'directory_path: expected uavcan.file.Path_1_0 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_u32(max(min(self.entry_index, 4294967295), 0))
            _ser_.skip_bits(32)
            _ser_.pad_to_alignment(8)
            self.directory_path._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 72 <= (_ser_.current_bit_length - _base_offset_) <= 968, \
                'Bad serialization of uavcan.file.List.Request.0.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> List_0_1.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "entry_index"
            _f0_ = _des_.fetch_aligned_u32()
            # Temporary _f1_ holds the value of ""
            _des_.skip_bits(32)
            # Temporary _f2_ holds the value of "directory_path"
            _des_.pad_to_alignment(8)
            _f2_ = uavcan.file.Path_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = List_0_1.Request(
                entry_index=_f0_,
                directory_path=_f2_)
            _des_.pad_to_alignment(8)
            assert 72 <= (_des_.consumed_bit_length - _base_offset_) <= 968, \
                'Bad deserialization of uavcan.file.List.Request.0.1'
            assert isinstance(self, List_0_1.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'entry_index=%s' % self.entry_index,
                'directory_path=%s' % self.directory_path,
            ])
            return f'uavcan.file.List.Request.0.1({_o_0_})'

        _FIXED_PORT_ID_ = 406
        _EXTENT_BYTES_ = 300

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8y|9F00{^90ZEqb%6}D?Pv2R}5V44Oh+G(K4HFCB|Q~}DTnxvuS#*T5^5DCF{?(VssQFeEhnO$FB1R|9H8EGXdvPCM;mJfVD'
            'LaGoF|AC*yb7uFxIJN~6k&?SRGv~~i=RD_`vw5=k@f#QB{GaNzd=$Gl2|`C!%S8W7_7e)i$fUV(x}dr`cZU+4;xXPC<y1edS3j(O'
            'QFp6Tq0Tb0wVJEWJt%A$6{V%aOP&uinZm`TQtm}E3kDj#?`c;A+w{|tTv1m`;T~D1O~!ssKWv|$*1fsj{BP<H>*`D>i^A%DS&*xL'
            '45ueVJXuv&&)?OQ#M3Z3VJr(779872=DFoF>OHJjc|UV{H>3Eyte{=8htG5-?CT;-DBCSm-4k#gNmqoaiK$j!sV;7f9kE$(8*>{x'
            '#V7i8y<Jyd4qYL$SlW2j(Lvc)o$3r_g&hIcnD*;xF^o-AS93MyR;sgGGLCh&d-!bXQuWp2542}=40s>nXZ8T<)t+$JOI=l0s!Q7h'
            'qdkhnz*sRTIfJ5f6!4ZWjdxI|+ow+T;%p+fBm!4w)%o6hZ;o@NE+9WsyXut_GG(nC)z!-nB}OrF&qJ`zqlckB7g9ngFlkb!UTHnQ'
            '+FMeusjsVV0JUlv_~$ax#i;J()t6d8!vVu|tljIqc}_%Qy%_crS65fYkxo;Bpo?eU>+0-xb<xE80IzMN)k0|Ux)LWjaig?v5{+E0'
            'Y*1=|LjjWC&&kTd*x8DTltyyZ52}}Ln=FzAWydb%L-R^Y8J7gszpz;*iL|35D^G=cGAXJ4UES?1eT2+EXu)_0tCzQBwoBWTQ=v}^'
            '>2a9KeLxF?pEL}TV_zP>RA-<zKVaF$lZEOu*Fu>{EbYzn(z%Zus)Y7)nfc=0Ec=8&Qe-3BI9O0-W}&i}WzQhnV(tlcMP2m;umniB'
            'bcz}BA4>_CE<bo@Ykhlt=l-_0SF-xrI5~*JlH))Q75&n-M_MM6LXp+-z{-e6!H}i9?K9@9=id5u%^dQ94*y#)osIQJ;k|b@zqj*l'
            '8;$y9yM_8ywQ%Fc&51LrR%YZb?2j4&Wv8XOrGBpVRizF}h)_&81~VkC532K^`#!~CZfp^v>^G|mp);k8DC9~FJ&@ID{z-Hn^x1;8'
            '@B8|FiX_j!39(UzmHN3{*H!2CC|5GM1FqI6;<69!hL(1bRO~kuQ^0bn5d_%tMz}24X>cRB9x&Q<!HTyMD(Mh|<w|C~(Gk_ZRaYLp'
            'zA!hpiCX~r!|sC4x?nHDjWCu94p&eXK|W)lGx7e;-R}fqN0BgDG7{jmj)fyQX3h%jM1eUd*%0C?Tq2zkm*2e1ZXJY^9s98^23Lip'
            '0WKR+7;j~bDMYLRDO`<2m&Xzlc}@s35JROS#aqNQ(6|~zf8_1FeA?BZvrPa8OltfhYI34W!EPWf2LZOj=|#qSwD!0H{5vWR6l4gx'
            'GAWcPcNH9Cqg0MWq_{r$?EYk4pRpGTVGmd`F-4c1P=-@S6tCXu2ysoUH_+uqV^OxtXOs=HfJur(XODTT!5Uj8O(=wrh8l))ifVAO'
            '!zo(u>PN<or!%eh<2`pcl~4_xmTj^d(G<SjV6Y=)9A!c}7#3E>bj=I~qEE$;Fw8v)Fz@RG;@|j>iSpU)$8CvYygLly&{$Vo!<9|!'
            'F>^>(yKO_Q$=)bSBpFq>)+S#ji5WWnnOGu1lNC~D42m4HOnaG%r~}^kV>P)J2K!?(X^~Q{AsnyF9=j$L*fV1;4vo0IzA5hB5fGo0'
            'Tu`g;tBpo3whoE+3vEMiM6@xxgT5+nrt98Pd01>`HTL`jtZ+tcN&TMvyrC|tf2f-!+7tEhruu{Wq^tg@{-pk_K2@Ko&(&Y53vXTj'
            'R@2a3N6}A8Uj6j|<^Ad6+}sXRxvhBtp+NGu!HD_L3G9HHh0GK*&Dt8un}qL#xH>TJTg8?yQKB(5CKhI}ie#i(18$vi&<$@1JfUj^'
            'Hk_TSGp*HCU~5uwU6i16;%f`SP&6)r&JPte1?LxIf4HYcT(UClBP1lY?M&RbIA_A2>H<g!wpe0a#<1jnAP%5c2YhhlBy6aOB@neC'
            'QYI+PL21_h_Sn9i5i@510?b6fDf1kdctl}oY>XY^23*8BEe1B$6IGH4Bp#KdBe)rj%^)tk8|~w+6An>xJdtG>H7ee~oRuQQ9fi}O'
            'E)&B60|h9VHG4X4fpQ4FampUJyL8|jXOfdQ;X{%*9PobM!!<?-jN$0n(0FdM24iqgqHSi-eZ-l`u7UQcj+(+{XNYMG%a8?^3((-M'
            'N0TXVeG`{!>^mLT;i807XhV)yzl6ht;>L;BIK@|x<p`2dAhsmHh;Rd1=2gTdF(;TqR!9Lsi}e6>&S=QAOW8S;fNbG!uflW=(PW}x'
            'T=6s5cua1wE6+f7)VOal+^4D2hE6R@J$8(o86qsad0KXwNz-`CXulYj)7tC^GmoR>-MXAB0(oV!#$lw!HgPyH^xSQ?U!9Pf+CWgY'
            'uH)nI3ps~yN<d7LeI`l1dOg-{+Q&$*3DRCCQ4;tFGq%k|yHOjZ<2$E6>L7cCY*^~6_y}!$q4QLqcJaB&lidcB>#HY8>)$6&)3Ha*'
            'vLA7`{r|0;ZK4G?<X`mWy+8|<;qO?VkF0B2=C`rv?dhT~T5*47_;1bPcOm)zUO2k?nepZ-P-pNd_hR!2cTs&)-TYrK0rk&`<g0(7'
            '`v;{!<a*<S<?15Z)aL&VY^VtLw>|PjCeSIr*L2FqCSw-PBhXEk4caHYu{M9~mx@X^aq172{ny6Q?AM0JiYK2OGs&jGe*o;k1h6m>'
            '000'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    # noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
    class Response:
        """
        Generated property settings use relaxed type signatures, accepting a large variety of
        possible representations of the value, which are automatically converted to a well-defined
        internal representation. When accessing a property, this strict well-defined internal
        representation is always returned. The implicit strictification enables more precise static
        type analysis.

        The value returned by the __repr__() method may be invariant to some of the field values,
        and its format is not guaranteed to be stable. Therefore, the returned string representation
        can be used only for displaying purposes; any kind of automation build on top of that will
        be fragile and prone to mismaintenance.
        """
        def __init__(self,
                     entry_base_name: None | uavcan.file.Path_1_0 = None) -> None:
            """
            uavcan.file.List.Response.0.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param entry_base_name: uavcan.file.Path.1.0 entry_base_name
            """
            _warnings_.warn('Data type uavcan.file.List.Response.0.1 is deprecated', DeprecationWarning)

            self._entry_base_name: uavcan.file.Path_1_0

            if entry_base_name is None:
                self.entry_base_name = uavcan.file.Path_1_0()
            elif isinstance(entry_base_name, uavcan.file.Path_1_0):
                self.entry_base_name = entry_base_name
            else:
                raise ValueError(f'entry_base_name: expected uavcan.file.Path_1_0 '
                                 f'got {type(entry_base_name).__name__}')

        @property
        def entry_base_name(self) -> uavcan.file.Path_1_0:
            """
            uavcan.file.Path.1.0 entry_base_name
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._entry_base_name

        @entry_base_name.setter
        def entry_base_name(self, x: uavcan.file.Path_1_0) -> None:
            if isinstance(x, uavcan.file.Path_1_0):
                self._entry_base_name = x
            else:
                raise ValueError(f'entry_base_name: expected uavcan.file.Path_1_0 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.skip_bits(32)
            _ser_.pad_to_alignment(8)
            self.entry_base_name._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 40 <= (_ser_.current_bit_length - _base_offset_) <= 936, \
                'Bad serialization of uavcan.file.List.Response.0.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> List_0_1.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f3_ holds the value of ""
            _des_.skip_bits(32)
            # Temporary _f4_ holds the value of "entry_base_name"
            _des_.pad_to_alignment(8)
            _f4_ = uavcan.file.Path_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = List_0_1.Response(
                entry_base_name=_f4_)
            _des_.pad_to_alignment(8)
            assert 40 <= (_des_.consumed_bit_length - _base_offset_) <= 936, \
                'Bad deserialization of uavcan.file.List.Response.0.1'
            assert isinstance(self, List_0_1.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'entry_base_name=%s' % self.entry_base_name,
            ])
            return f'uavcan.file.List.Response.0.1({_o_0_})'

        _FIXED_PORT_ID_ = 406
        _EXTENT_BYTES_ = 300

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8y|9F00{@LyZEqY`6<*hAVsD$K!H^aZ^s-dQmYhj~qVgt?OcGPH@y2!Bs7OWAyEA9^UNU>{Xzq;H8wrsL0Y)0spiH5_2R<Mn'
            '5E6fgKf=d8=gzEmH(9H-wA$Ho?|FO9bIu$;KKJqeF1Gw%`9?a4U7Q4=qfE<0Ka%}~f-th9)H<D0RbISJi5}rGKAfafJ*~DrtbSQ-'
            'mghrl3}uySl^5^lSrO$$MvGTo42>MY#Fq<s6iE{dG;H71E)NdKrPer{t%XOFIc*Iay6~WRep+=~-Id=~A6Df{q0IA4_luld^>bJ~'
            'BjnRtRr&J1jALzvyPA@C7EU{iWiG><V=TY2+{%&FF@k!4ulZaMMPKJ(LS~q&sw-SywaZpjo(p3eRpsl*hq5Dz#lU7_P%spta1>NU'
            'Uu~2xE(W4rR~MS6cKPZ&Hv1CR)ywLY?n<}C*{jRQSbcM<SAO-3+_Owhs`9l55>iO+`Z#x3x>%8mAtf{-lQ$@wfn}O;#q|+xY`kln'
            '9vX^&YH}J<wqQ?vy}JfjBkA&RWMit-&GO3rRGF^^w{W({M_kh1R0mc0#n9!_#4?NLF+C~z<vJ{-GSc~^>Zauvnxk;Q=+yzMw`Pvj'
            '_tX!%D{NBzh_%m!{lrz}x27r0j3c}J+23Hvk9A%Hbss;cg<cJ9T9x7~BW^P4+eD-08+$ae04xVz@1>N<+-CFL5h;zDtGnfwZdnt_'
            'oXpazoHXCe$S}Kc|5C3=5}8e&yLmo5l1V|;N7ZI`?FlH@YruF1TCW{QGo%AbDc5I(^e`OBV?YaqpLwBre`?F)H_`@0;s;#Yd%Rj+'
            ';Hnmh#MSN!Uu`{cs5c#_()d2@6@5Y=3f0hiC#&iga~IVJr)(K4KbLxD3-yL?h&4dMB*^D`VzIP8^hJg0`u#imI|n<5_YS<idcXYI'
            'v^a<(BgcU(P<HLWBQ2Aub?B@QG8wTH3|ZT4o^f8jaPvDAbI1ppeO55-y`A^MyLWm&Iefc`Mm=g=s9%+<H*S3U)EJc;bCWCVPwHXF'
            'MpLz|#>%PRsb3eEEHNPsW=LF}l&^s9#}tRD&GHbls8?PNoh`D6LLL#J2eQ1tUy1I6KKq!{$9`};MUhvoVJIofQ}=~bS7rOwBvmrG'
            '4X#$09z`GA4Ko^|sPH!%h=ApMJ&B;tjxhMyXmBIA9x&Qf&b_-4D(MhI#v_DBo{p&cy%O(zW3|=lk%LXa=7RQ)U@O8+AR7q|SCEM?'
            '2x6g)c=vGkyMZ`VB&<m$0=(9-a0J85S)rZCafV?!#+VQ;kxq%uwGNwg80>7=%Qhk05*ZEf-VnL<TA8)Eh&3REsfpNRSz;s431J6f'
            'taPN<MN9*Y!6y0>ujeOtwiUDw2;hK8wOvF_PHa*z3`8dg;11af!#)~)3^V^59R~_B1e-F+l`Vz}hT&)=Cn8eZpPakT%)cVw3yp9D'
            'ESZ>MlZ}u;))B>9-){?XRqWKzrB>sT8FG%YMiwwhk!bUfWi{4tnbe^WLK<r*${DJ`*#>85!K#-`4bM&*>&q>-xs;e1dQ>#Uu7{@Z'
            's{?}_DeK4x>7bZrGN!9`Fc5vp#{@C&8^FA;6Ab^_eoU0kyPvKYj`40Yh+~_%{3>2P#1@T1u^P8EwN8DbEm352;dWDenIv}X`0G>?'
            '5n7W=Z5R|eWtsM4Dxx-c<I}2ZEiC-Qnaog9?jfXCn1`+|1$-Lj;@FB?J3X;`TVVK%$OV<Uqu#E^MR#F%UuqVX=Y}>;?_ots>*K1s'
            'RxA$N`5Ai&Jjy0vA9&QG25tHOl~#+PV4+|kH-K-FDYdzxP}>$dpkN#FhWkx3Sq!giR))YA`Wa!33~*-VX%i&{cR371yyBs$;NHYz'
            '9iuSqJEIg8)&t>+NY%bYY^heJV_pv1?Oo82j^!v#Xd4$(?4rcspz*YuHbCdvz}jnlnc?#&=xfsn1TUAK)rfKypXU>ce4sPEPCXp_'
            'C~3>wUtxa3hfV8O2)ezNYZKG4xDHz&O-5j%5uN3Z9pgOnzF^>n*yP4FleW@BB($|)P#QrVA783YXPdP&k1lVzu@r%~z#o$sdNNWB'
            'b`yD1-GpJp?n&wo;K+Z}n@)XnqMr2B9~C(DvHFwxv-(8+Mg3L%t-O5m`djr<ejUU9bkwWApZFKtQpW!C^l2u$UtfE`OU$yH^BafY'
            '?d9JMn}yQ&Ov$YNQ7;sm;P}6096!DNjJ)Q)dI?MOtM#&cMZNhs(pLYSOA>ny9b-YutGy4_%PV*x*Z=Wkp(0GG?77`jU?;d;?*vQn'
            'naAR}yl2;B^AzuGuPoikl<Fbf57zx&wKl(3d64+<@sdMU4L$`*vh`Tz4FCW'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.file.List.0.1()'


    _FIXED_PORT_ID_ = 406
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8y|9F00{_)mTW=gm6}IDSY)@_*!e+xp3xyZ$j>)9sz>2`W5N|Fln%J=%Cj_BYr@FhwRY^~GQ{C<HM68rZfD)+@i?#s);tmo#'
        'AR(;~62E}o0e^xA9{5gG&CMReYT<=Qv1jUX>eP3>^PN+EeE9qN%#8V0eIn~ec@%qoF0|sYdc=cRcz&36vou$QsH>y5h2Bx2*y?AZ'
        'ey?7BQomC-tK+^FUoS;o_yvv2nd<m85vwk?M3XCz_$o<+HcM_7x(tg_?=kkApYSe@I$QFckSAV8!H1hFFT72ANL?-XJ3{9wO~}st'
        'UHAFDx;@jL{dWBXZu-0^v<k{X<n`Mydce(wtLo~x8%o5{$c=^{@q*h69ke~ubVs#=6{qhcx!O)d^yQ=w+d@y?>8Ky5!jDC=UC6r4'
        'U_9hNtD8nZ>*Lj#je#NB=3T|y8corSzEyA5)kpoj;7P=FG;Zi=8OW2>QIQn74_qU$TUUquC=KgsrpDaa>evR4B9&}U-c7z-y)^wo'
        'JE@8Q?_K;FzkqzD&2pS2Tk?E$c2i)}j)+(%)vQxe1X-C2kB)q4aDqJMKAo(d9}naPhvV{;Jl&pc&rq!78N_F_uR3=?q_pP!x_a?0'
        '$0$Z_8VFWtbT1c0EV{tNagjO8ue2BBr({zu1GQ=q_-8y+MZa!m)khqleurS1y6@HYECs^uKI{i^URSRUJROAuP8WN>*VVB%Rbl<T'
        'jjztrYR*ryx?%?z$@|?PjTK^fdQEgw;81|%w=$u5k?Qe`3Z+7D<=yIqt7#JQLL^g{(xqvo773*U)}LH2<CyFIzLiJ(9UhmW{%+lD'
        'FT9J$-*aGm4ZB|4<jJ<!6qzX0K`uS?yL=bWVnb*d)EU?^_;pnRYSRZSTYEfL%~LLvF~`#OEG?aRH%FF;-HazDx!21;z!8mT<ZDmo'
        'WHGi-_ApD9LAJx0A=r7@G6}E%NGNrRG4fBP1hy{TzP_=#xw>_0)9ja>>g7Rj;D;7DIWm#-3!4UM9uE_xQ!REh4`~z(S-9aoW4=1{'
        '`sJE9WE}m*e{!a=wtCOMd42s$TW>jU<Tu?B@>w-^>C$J0#zb{`Oz!-kZv~W$K9XOQPvkrDd-6LaL?{xt1~DY6pH?S8_gxYBS*i;k'
        'X}?~b^7FLRq3|hFeFJ1QPrqUnfIb_j0lOxD-$RgRFG6f&N=khwQ+3t2+Rr49uYs#IlDG`OU6h4w1Qq9v#1ya`v4Vj8bWmL#C!^ja'
        'Z^a|D>w*;Tv@dxMA2elhZi`O+OrF2@$+?-CbyNZ951I2CtBkC$ypORiBX^ldLda*tRKo6T-T1u6wxnQb689N+ts<5S7$(j#m9qkK'
        'P_iDxmE|$dC0n|<L}qgcCmA+lO$;tGEjlPRtVqo+ou&ng6d;AEK5NogoQ8%IEbXwKRH39JBGFMO4J_!JeMUa@ve(!Y00&I6cHy<i'
        'SyOo19$WG}9EaPpgwAmLQ3A|&WE?0+5HxvQ$h6#+FpPt`yw5^O`AK&-H#7Q-vyccoz><i`nq)*IxOFI^<u@9PU0|ygx-3;#lx))-'
        'xkVN*aTcrOA&ptAab#>=5pb!eu#t~Y^$s>TLJL;S$iVPu##x_kxj~_XYN&4Mf^9{UnRbJ~4rQ8)gz+333(X^OA?<WnAc~&AF!eIP'
        'JWw&j-`bCa$i|N!v?V#=-5?Nqsm_ZFDA|H6COLxTj<wVpo{h9bkdcKg7knPaX)mW=!=3OjO$x3O0)-D)ri@I5q5<BRYuQ+{6zAhG'
        't`SnoAzZIa9_BU_I5QzG_EL6rb)DU~#vndjk$bhgB{!{H+?f#Xldd7yC)$|(D*CF-PS@>)a#C!^HTJ|1EPqUGh5RAe`LsMI|0FM$'
        '@<&hQkJsf-<j<P&=kgcwm-1Kg*YY>=x7DfFS3YMOx)mh-Fy-a%pCY|~dU$4Li>T~!o<S%OJZdl^x^#?vKutqt3NeaW3+XMG>4Ydd'
        'nCnL!U&2^nYCtT^V3pvZbQ`F3%0M@Ki(v^}E3l#Hyf)Tay#{R4E?Z$G=p38ef-n@;gxC0r6gJ_^Vw?~2!iq~$b_2MCz`D*PA0+3P'
        '`y*WdDZv&kNS86p=?BCC^lE?)c{y|&YN7>*YKfFE(ak_<(tdYs)6TH5I{*P<BH-j%222d1*qQ1GCqx!p_&G`j+N_4E#A8T2GD(Fn'
        '(;sYuxX@{07qyP%@S6MyHNmKm@hP^GQgl(Ha69B>oRY&p0ZOLR9ThpCa=31dk_GB6b8wC#Nx>WPA&zrg@K#{p8XyG5koUAPHQXi*'
        '#$cyJ+f1MvkCQaH0NQs|XcL!=!KVQ%JrZ0>z!bF}O(sM67L=}$>2&f2B_)hP8!~(~OUO+qZWJ4hlT?B<c@XzKw!r~Lhzh8QS0QbQ'
        'D8S^hL<j`5Sam?>MD&PuT`~?O5V|nct4JFYG#RQGW&9X629r0)lwlwlvgU1s12Hmc>Eu{yup{Ks9^Aq=L(7JpOs%y<>=uJ`YK@N&'
        '^T<m&tx2&GATN(w<VH8u){mU^40qk}%R_Pt=Lpg^Zx}z!LW&`b3LvJ0-V-E~y#{L+_5so@CX~@hqy!#esdlk&2RScusyRWwf#?<7'
        'veabpKH8W>r>Q_}<GD(cO^eCO@<G!2$Kj{Z*xPp5ed@OVyOrZjG^2+6{r0R8XeM*~AL#SGb+%=`f<;$Gi{5wQzGwIkcJW(~{J+la'
        'U%hACmIC=ao^mhPC)_!CQC|L_ML_;}DEaa)=>9<|5V>BvzgV3?n`-}dpnWM&zxBQs8AGSMZad|v!5D{gA9SN-58bC^tu;IKr6Tn@'
        'Zhe2zyfzlbUmFH1ntVKE(mZlb_)aB+bAR5Q));#le{9O%IP9i+1gtlFD}44tzsA3S!%o^t5TK2*F9ej^f6P+31=FdwNsRt>T;{lr'
        ')D;k<wI{q5#$C(mdf>DqQ6DOlEd_f9Z9}7M8Bj?Wmys1FQbZ%-0g}3>BJ@*@>!yl9L&hrIu!e|TWs3R@+!ghvo5iAqg&71}49n!8'
        'Z(X|BNz;n~*ZBX)3skb?v70X0CuP;Nfiz?s9qn7PJ-vAWG@M`wTLRL|zWkOa6?J7GaHNiGY5KvY&W%o=FmTCeDNp(hskU*U<q3lm'
        'Rh}&^wP=?Lxijr7Il;sO%Jm`9&~q1E(mY~_N!JI9Ai;xq{K!90zPA2%3OGgA7N+T%)21d8?srqPY0tRTrUx^)(J+f192#8mL*Dss'
        'qyvBd{}Q3Se|#enjtR?19u}~2-WB=5A5TWJ|HSNq9tzV~xBuWxg7FIdxK2N=;)fOewI9s>8%Up#?3aP}FXXSakbM>a00'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
