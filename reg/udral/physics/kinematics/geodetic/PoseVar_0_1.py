# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/physics/kinematics/geodetic/PoseVar.0.1.dsdl
#
# Generated at:  2022-05-06 20:34:36.077038 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.geodetic.PoseVar
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.physics.kinematics.geodetic


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class PoseVar_0_1:
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
                 value:          None | reg.udral.physics.kinematics.geodetic.Pose_0_1 = None,
                 covariance_urt: None | _NDArray_[_np_.float16] | list[float] = None) -> None:
        """
        reg.udral.physics.kinematics.geodetic.PoseVar.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value:          reg.udral.physics.kinematics.geodetic.Pose.0.1 value
        :param covariance_urt: saturated float16[21] covariance_urt
        """
        self._value:          reg.udral.physics.kinematics.geodetic.Pose_0_1
        self._covariance_urt: _NDArray_[_np_.float16]

        if value is None:
            self.value = reg.udral.physics.kinematics.geodetic.Pose_0_1()
        elif isinstance(value, reg.udral.physics.kinematics.geodetic.Pose_0_1):
            self.value = value
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.geodetic.Pose_0_1 '
                             f'got {type(value).__name__}')

        if covariance_urt is None:
            self.covariance_urt = _np_.zeros(21, _np_.float16)
        else:
            if isinstance(covariance_urt, _np_.ndarray) and covariance_urt.dtype == _np_.float16 and covariance_urt.ndim == 1 and covariance_urt.size == 21:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._covariance_urt = covariance_urt
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                covariance_urt = _np_.array(covariance_urt, _np_.float16).flatten()
                if not covariance_urt.size == 21:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'covariance_urt: invalid array length: not {covariance_urt.size} == 21')
                self._covariance_urt = covariance_urt
            assert isinstance(self._covariance_urt, _np_.ndarray)
            assert self._covariance_urt.dtype == _np_.float16  # type: ignore
            assert self._covariance_urt.ndim == 1
            assert len(self._covariance_urt) == 21

    @property
    def value(self) -> reg.udral.physics.kinematics.geodetic.Pose_0_1:
        """
        reg.udral.physics.kinematics.geodetic.Pose.0.1 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: reg.udral.physics.kinematics.geodetic.Pose_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.geodetic.Pose_0_1):
            self._value = x
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.geodetic.Pose_0_1 got {type(x).__name__}')

    @property
    def covariance_urt(self) -> _NDArray_[_np_.float16]:
        """
        saturated float16[21] covariance_urt
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._covariance_urt

    @covariance_urt.setter
    def covariance_urt(self, x: _NDArray_[_np_.float16] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float16 and x.ndim == 1 and x.size == 21:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._covariance_urt = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float16).flatten()
            if not x.size == 21:  # Length cannot be checked before casting and flattening
                raise ValueError(f'covariance_urt: invalid array length: not {x.size} == 21')
            self._covariance_urt = x
        assert isinstance(self._covariance_urt, _np_.ndarray)
        assert self._covariance_urt.dtype == _np_.float16  # type: ignore
        assert self._covariance_urt.ndim == 1
        assert len(self._covariance_urt) == 21

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.value._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.covariance_urt) == 21, 'self.covariance_urt: saturated float16[21]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.covariance_urt)
        _ser_.pad_to_alignment(8)
        assert 656 <= (_ser_.current_bit_length - _base_offset_) <= 656, \
            'Bad serialization of reg.udral.physics.kinematics.geodetic.PoseVar.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> PoseVar_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.physics.kinematics.geodetic.Pose_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "covariance_urt"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float16, 21)
        assert len(_f1_) == 21, 'saturated float16[21]'
        self = PoseVar_0_1(
            value=_f0_,
            covariance_urt=_f1_)
        _des_.pad_to_alignment(8)
        assert 656 <= (_des_.consumed_bit_length - _base_offset_) <= 656, \
            'Bad deserialization of reg.udral.physics.kinematics.geodetic.PoseVar.0.1'
        assert isinstance(self, PoseVar_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
            'covariance_urt=%s' % _np_.array2string(self.covariance_urt, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'reg.udral.physics.kinematics.geodetic.PoseVar.0.1({_o_0_})'

    _EXTENT_BYTES_ = 82

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8T!wXG0{`vX?Qh%09S3kdShg%Hj{KCkPMWZ7mO5#oQWPms*;Bf7SpYVf*Yv?nmui&6_~^=_MpB90J%H`7Aq5DGKsg}5{(=4p'
        'eW|_c+o5l|m&JfK+nZq+Fa+3u?N0ojWHWY?V!+;12GZa0>Byt_xjWvm-o)=dQ4)hc|73Tk<+R$xx?|X;-ZtOS8*QUlZ(3Vj%Q0Oe'
        '^bcKk?OxOE*~Tk7T_gM;Jo9e&i*VJ?)I0hX-G1ISHj2HLt+$I^vg4Rdr}(znF}8G<B{vMKWzbY{&2o&_bUXC3_1lK+m{unw34iJ}'
        'q(2C?gqHkG_-^RW)OFXj%|_2PobV<+(*f5w+$;1mmrbMH8eLni-qKyY?y?Iesc0q1_-7ygQbRIDruik2JiQE3Kt2n*a(wP_b2K~d'
        'mt}cS8N0T*WxD2VTE^+iZA*9e{suGkhUwPZMrXq%p>~m$yQw>FeT$wpB&Yl%Yy5C_Sn(3wc9m^nH~ZJ&%b~wmcU-;G((TsnjPBBW'
        'w)BmT>GoRe#J6m{>Czv`p+DYbq-h@ON-~isRcqBstz0V0YDFrSl&YwfWJRjVQn^|#RYke1RH`*qtco-$lA_9TtyWQLYOPe2s})sb'
        '$4C{is*0kdDrL1=5f!zjC~BoFRVx*>s+OuHMHXeYwyc!ovMR|Hn!Q|>N@b~{sx`V;Qt8gBOiw}oiDji+RZ5kbS`q2lN}^J&C`w6E'
        'C9ztOWJRutVofZowX#GHmc=SPnW~7YOm`}mYcy|mwz5>N(7hx{s>y1pqNt*(D77*@t5l|?rA4GgSEY(1$|YH@(!$e=Ez_&5mQ=A;'
        's!6q)s+J^0q}MJ=m69r#Bw3~TR@9K){9c1TKiM{YQli^DQEypIdWYY%^_Ho3Zn7OlkKAdb&S)3OSyCj=-z6d`kAH&y{U?}iTb+&Q'
        'Hz4Xkw|^vF=;^ncdZ*}^#U2$>jLZ~YH(SQ_rrxGC+<<vfOK|4nU-AF&D`vI~*Ra_yn4l|ke_>Z6Qg7@;ZPhPA@-opJT5YzBu5C1R'
        '*Jy?B`?K|1=C;wQcP-nko2~GgKUa6Gp4~L)hPF}f>a<eyr&ws44O$`62EyE4V{1R4m2mQTikDcdElhRI(9d1k=@PyDqOoO#{;_Va'
        '(KefP+D`P^?0ln^iB_kR(ZfU!bm)N-?17>yQ4RYGqlc<kDvCwcK!h%<w-@R}cj$H5M#p6>#%;4{gzpoTT&LAYqfK)@&D)bvy-s&@'
        '<IAC+|DNf-G+4e)7tyl#>AKYoec_-?oSm(PMT<qR<SH#DZLL_F@WZZQ>#k*w+Na5SlbEz&CSCvVn%-)eosEZfB0aYCTCYuuxf9<?'
        'bGWUydq()%a8<h)I1So;=tdcZTDI4q#oaPHtm&f(eVZkwSo25kHOpH|vf~ngmO@Okm<+TDEN57p2((GWDQwST`!tqw*gnJJbfD$2'
        'e2B$-pv|(F4Yb2pU%>HmEFKE9c@}elw!q?4pe<s*CFFmE#l=87%Hn*WEwfk%v?o}c4YU=U=NR%ij`Kaq;$)zmKz=7#Oa+>N^FPJn'
        '$v}IW#S?+{42w?&+9?)~2iiASJQirDSzHOUXIXqA&{kPo4zx2Y9u2g!EFKB8=U7|{v~#%L^DHg|S`pX%Jd1OICgS=_EFKOt3FRo`'
        'e#j_~!s1MzRZy-f?yrjS)o{Nqpq$@iF%xLtLV3T<Vmi>igK~ct_wypke<gZuv~@&+xQ%!h@gCxbh#w(-jQA<yeZ&V*yqZlSvCI>z'
        'JfZT$6`ok<3BnWGJaLyN?(xKjJn<1ve9RM{^2B|fcz{HY_S}r^uHG5+sj;r%G@`zS-gbxWocp55x_(VVXc+Dt!{`VuF@&~7Ya3z9'
        '&^v--=tA4LZM22etJhyTBhYT*V3%8iUAnA8D_FM%tMra*bUJ!bVD%#FZ3_HMg5I#`BHM{(QlvGrL0)0ztK@0&0=Yo`OfL1vYwwfS'
        'uaR}~<|_Fyxk=t4b@CHGO>0cru^;rUS>+q`u4(N$>R;2&67OM${_LQSO>4>0sGcN*)`|Wfet?~X!7B~DGZzHj?K&q6TmN%|BJwLQ'
        '=3b!}ZP_iu7EDKI68cU+?~x_YQ#VOe>}|SXum`P;_`SIH{TBt=U*19nj`@x;$hWQUSUub^dYHrCsaWR5PkZ#1(!5y)mvoypS+obj'
        'u9n_9)^QJsN!o+@kXXbXR-1Q*DSKB{x^&6vu$HZ}Z=LK<M^!RyIoP|^BXWBXo%CM^?fJ84`!9LzOgt?~pS5>s_vStN?^ok0cw7a4'
        '-Kt>n8LxLA;$b+<hDU99Ut%K_vyq046l|noHd3&Wg^elL$il`9Y@}c#8?!MD8!6bBg^et1q+nwnHV(l?7B<qbu?!oFuu*`GJZxlP'
        'V<KkbN!VC{jia!!2pe;-F$)_ru#tt03~Z!e<1B2f!p3RXI0YL|!-fDGCt%|^Y^=b>GHe`yjYZg)hm8Vk%)&+<Hgd3$g^fwrn1GE`'
        '%!UdZtFW;Q8(G-!V8eqA4>mm5@L<D(4G%UvZo}g?JZ{6|Hau>_<2F2Q!{atQZo}g?JZ{6|Hau>_<2F2Q!{atQZo^|XJl1_5YZz-7'
        'YoHFCsA=d^4E-;`kceSO0Yd^9(lHEaU`PQ&1{e~+kOPJsFyvzxGQf}rh7>U5fgueH1z^YmLjoA)fFTDAX<%3ehIwGf1H)tt!!cku'
        '0t|D&kOzh-U`PSODPRzQ;W#iX1H&RP6o4TQ3|U~90EPrGoCk)p!0;?EoC1cYfZ+r%90P`BU|0f%d0;pU40&Lf28KysNXIaUz)%2&'
        'bzryx3@R|J0>d&eWPza%41Hke14Ex<=yMExj-k&n^f`t;$I#~(`W!=_W9V}XeU72eG4wfxKF84K82TJTpJV9nZW_iK#u~o%8u;K1'
        'AG-+IDDMGt6DMPH6MAQ(Z4`gh(_O>v430f;YQjHuz$B|}>pP*pc$tlmN8`jVuvL5KArIA!wz0(qqoXO;(L9H+Yo5b@wk(U1DwX9*'
        'rK~EFswy?L#O5|iYFSogHq#&}vMgd)pN&=MUA<|#JE1nQ{}@QupMTlt8m_tj0CcMUHam3hNQDp#ZtA%2IqrLo`<}dlnYgpP^A0K('
        'oek1%Zln{5&A+7*31{CCTB4H%Y5JK#B@_A!qiSaFWYu60mRx_t5a#B8=!wQJg=3gwm@$|$mTl6ORo~V4N0TU<pEEKmn}1|Zzo6;;'
        'XHv-L<O_12{Du70Kg7Ol+HZ>F_csjN5^O6v3!9T*QxOhbG=w|EunkOj7!IH3XjrYCXre>VZ8qU!Zgh;6aL07XL;FUvO2e6v3%T`Z'
        '{>TwJmhF;r!W(?q&>i=jaDy+ltUH~rGWqeS>59LPUoFP37UNe7{%Wyl(VAm0@O1TJlDx<M^Y~3}BG%+)Vj?mSk${L~tjWznL>?kC'
        'F%h#6F$)m|h)6(01|sqhu@q}^7a<}G5l0~+4-rX-ScHgNOvF)$n1zT8L<kVE3=sv0$U;N{BA$YX6^K}Xh&)7OAmSWEoQ^fQD-f{='
        '5wj4Hg@_bHNDy%zB32>d8HhLm5l=wGB19a9h#W*@Vj={HP$41<5o-`3LPP-~?m@&|h}eb*0uk#FafORexrkLRVwsD`LIiyxL1K_1'
        '!_@XLb$6J$H%xsvOno#=eLPHkI!xUkrXKKAq+^g8jzf)cjB$){#BiW<nu)&7i;qcd{)2W$qlL|XvR>+FK&Y^LKqymD6j8=-&*s1B'
        'p4!sB-M!6JdYEA*J=ksUm`(v>I#<^i*0tnU=-VY@eY?Z~eY;6uos9ME_{(DgSSJto_JsHC4gqTcSQEfH39PfRzTHgh<uMPe31FQA'
        ')=6Mp0oDSrPR71HS&H@T(!eSJ>oTwwfHe!O31EE&SdRni60pt!>r||7cNSPr0qcp_%i}z-=7Dt*SQEfn2G%05o&nZVz<Lr`SAca1'
        'SPT4tUEB4*&Ni*vx^1#A-|9WvrBCkqC&@(O)o$0Y&)en(aRrxc-e?>A^<{Jf`}oT?w=d*!!oz=WMxWzG?>IMyYX@Ij39IaV=?u2T'
        'j&^Om<FunUFP(jk7JXU9{)TU4dV_sE#@6q1>UG375N{l`K6dPL=fB$D;Jqyxg=UBUJom=l<x$RCZ%M*_e_Lm5y_LHW%VvF4PGq}h'
        'S$O0h&GapaX1nLG;m3xXi43iQ<~CoYVKbR|jQ8XM{%56qUX>p?koEYlqnm$94~D#w@lFQ$>>8~N^BLYb4^ng!{SV(X?3lziuxGsZ'
        'Ul95P&fYZu00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
