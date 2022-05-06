# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/reg/udral/physics/kinematics/cartesian/PoseVar.0.1.dsdl
#
# Generated at:  2022-05-06 20:25:55.322590 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.cartesian.PoseVar
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.physics.kinematics.cartesian


def _restore_constant(encoded_string: str) -> object:
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
                 value:          None | reg.udral.physics.kinematics.cartesian.Pose_0_1 = None,
                 covariance_urt: None | _NDArray_[_np_.float16] | list[float] = None) -> None:
        """
        reg.udral.physics.kinematics.cartesian.PoseVar.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value:          reg.udral.physics.kinematics.cartesian.Pose.0.1 value
        :param covariance_urt: saturated float16[21] covariance_urt
        """
        self._value:          reg.udral.physics.kinematics.cartesian.Pose_0_1
        self._covariance_urt: _NDArray_[_np_.float16]

        if value is None:
            self.value = reg.udral.physics.kinematics.cartesian.Pose_0_1()
        elif isinstance(value, reg.udral.physics.kinematics.cartesian.Pose_0_1):
            self.value = value
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.cartesian.Pose_0_1 '
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
    def value(self) -> reg.udral.physics.kinematics.cartesian.Pose_0_1:
        """
        reg.udral.physics.kinematics.cartesian.Pose.0.1 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: reg.udral.physics.kinematics.cartesian.Pose_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.cartesian.Pose_0_1):
            self._value = x
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.cartesian.Pose_0_1 got {type(x).__name__}')

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
            'Bad serialization of reg.udral.physics.kinematics.cartesian.PoseVar.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> PoseVar_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.physics.kinematics.cartesian.Pose_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "covariance_urt"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float16, 21)
        assert len(_f1_) == 21, 'saturated float16[21]'
        self = PoseVar_0_1(
            value=_f0_,
            covariance_urt=_f1_)
        _des_.pad_to_alignment(8)
        assert 656 <= (_des_.consumed_bit_length - _base_offset_) <= 656, \
            'Bad deserialization of reg.udral.physics.kinematics.cartesian.PoseVar.0.1'
        assert isinstance(self, PoseVar_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
            'covariance_urt=%s' % _np_.array2string(self.covariance_urt, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'reg.udral.physics.kinematics.cartesian.PoseVar.0.1({_o_0_})'

    _EXTENT_BYTES_ = 82

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8Q-pP50{`urO>7&-6~`$`lqgD;WlORZ*|FD-W7D$D>^GNbk~(oBxR}UMoz#)j#@i*i)+|GEiQT0t1vRiaw6K8%x~R8+dn?e3'
        'Z|%{iz^(gX^eb(1F;JjDZ$9<xW8aW(Nog(BNqY<li2t`cGjC>>^PBf(Y=7h@|9&ym`2<H>n^m`3FX*o6SVrCY*eKV{f?ly3E!(v`'
        'GYa;+>pAU;*LKYJHd|(NJ39SIbR)_K8NF#VpuFIiYlU{zG3tdD-E^&rTlmOonhnEaX2ozk)3uCdVa0aMD~1yVS$*AfT+41oG!=|p'
        'LHl+@Qe^0d(I-(bp&Op(Smidfj6Q^}b{S-^Rup8GEVEwi4=$%y4bRX$He#CY-lUn}%$FEzM91iOJSI8`<Dk>%Xl9GcvtQVy)%2e7'
        'xueTtZDYLxO<b$cZdzWUZZ_9ET6o{8npez<XFF2Y&k#vH?I$?2%gb^cV>1e7m#hu5`gX_T>+II{A9asz*3E|5^t!KZw>RH%tcK-T'
        '>ri8SscswIb}tip+4A)6up@FFevOLZdV0gI!dn%C11oWJ)~s*=%9dFXn*u+GF2f*o*E5<`!>Mj{bQAnEj5T;8?JDc|x?@y4m^v;@'
        'sU@_*$Eq@vN(seMQ7uV=Bx|ZD2}+UI1X&S_vM3cLp~%aUq83XUU*tg*QPE_%R8p0aRuYPGQPp_XMpXHt#`B`4NLo?l6|JNwnktD!'
        'Rn>}`P!trIm)TuO5oAddWfk1Zk|;=`s%a&-6f~%;$<PJ-@sc7H6+ta&Di6I0yi!yZMG!TSFRG%f$R(aH@sd`OL})DYMd(aZcuj^%'
        'l2iiUtT#!NRH!A2VoBBnRnd4&QA!f@DoXIQ@QCo}ny8ArEXZ;Z9v%iO!Dx$u#+QVWSSo3nASyhJoflO>lLb-Mz^|%B?B%!1!8rU}'
        'Eu&(2n-LifM)YzWUh&CzCiH(1m=s>}ItnJ=u)Oa4dKWHnP6Wfc-HHNkHz)39qiol$N)*g2n++T08T&QgX_<}z^SwW_M)eA{0Cc(>'
        '?7wWbOwZc6URwVM#!fFoy}g&(^}69~CM$ujb)()kqaQ_iaz1p+@Z=+U!)iw4J~NCBW{j~}+pZhTD;Z){Qz1#C4x^5sW|*c!GK$w@'
        'Oou~~#p`jr&SAX?rkRjTV)-7XxsXhu?qxa|l4&g8hxPa4{TcK#i`R4L{{YkJkQ`*14aq#Ve~#(CkSw78Ls<VX)A^7*&vbuCj-bDz'
        'Oh-e)Vf$lD4~677(*q%S0sWo8`Y$pa3&}|w*D0naLXv07h2%8T!y#G3{?0I+4ar#??>Y2Sz;VCCbR;A^_Af9!7ZQ=_Vn`&Wr$QoQ'
        'KMK=hAyJtg2}u#ht6_g7rgI^A8K3iOO!tQ573}v_rsE-b4WIk#_<qh~{}-9^Az8)oQl_gR*<gAxBsZCAA-TgeACkM+?>&5;hfME>'
        '<Pqv))F)kC&JLk59~=4D&|>3aY^=rxjg5`ixEULFV&iUX+>4EevGFK29>>NLG}^G>nj0;n*$L2iugpM!AeCvDo(a)>M6cR_Z3-3+'
        'BbeC|x%Kj9H$%7)(ff4Kg{V+9TaH;VJhK|z3a0eyEEMT2+wpX(8eIzZ>8{;&Dkc=vO}%BnnjefYsas`O?;$8#8!PPYZ6JK;CFq;l'
        'ECU(!Kn+-<hSw}ufN~c$Thyq(3F}A%(Xd^Hbw!6L4HQGq{lowojCLb!6r^1X+_7j2H!<D>vs)r=K`8JAwsu7xi%>H<HCz~?!$Kv*'
        '#&xS=Mz`p%=&$J#{YGbfp>NZ7FerDHp%tTAwVG>BtyNIE0y$BuTO5%ryxwc%KGosxyMt9{u<Cr(Rvr3ja;fRYX+{?;GW5ZXsCFK5'
        'JbK)vzr96&cZvR<{vl8QNdH9tO#ebZqkj#C0e9FGbkcIRhIA8iSQ`4NIV>o><U9(dI_WteF7zR%j{xXk@j_gStJt;!jKV77a`tu3'
        ';99H^XEiw&(j~JH?acl^d)7bbzXo^@@E+j34exB{q@i;j&>?)sJ@L`Rp4e!v!AA6(ZGh2fcG~W`Bc=tk1S+FdBplV~EA-Wy^fmf='
        'a7u!$kOq4<Rh2YF)HK)#3T&4sXt1S{*`7^QU`K`<B>EN^*%|fs(0U&#T&7pM6~5D*sGX<1MtmUO|1adH6XXvg`Dr9SoghDr<Y$rm'
        'F(f~W<WC^^X(T_JAb%XmPb2wLNPZT{Pb2yJk^DVKeiq3eM)K#8{8=P_8p)qT^0P?(NP_(5k^BWD{~(e-i{$S^@~4pe2_!#@<Y$ol'
        'G?KrF<mZw6lSuvvB>y;)&ms9oko?0){sNLekK`Xf@@J9!{Yd^al0SvyPa^p_BtMJfk0SXaNPap&zJ}!Ik^FfiKa1r1NWPEc`$)cz'
        '<oigzkL3GEz8{nC$K?Al`F>2kACvFL<ohxCeoVd}lkdmm`!V@`OuiqJ@5ki(G5LN>z8{nC_sJjm-p1y~+v0jYol4d2L2%zKw9~)Q'
        'zthiyOoxBS!}}}1_6)rfym!mSdl9+zfaMW!P#&N;Ky!d*7tIOVv0!g&Y>CSzBQ#(81w&?`_G3osFTrl_LTc>|D6CyzUvILnx7gPb'
        'd<A>h@%j$A_A_zawxOQ8U^m%WLUYHXLUxGBP6}az&i)BuNBEbw!avB!2O0TSJ|nO3K(*-t56kC=sLsB=csNWY!eJ&sL<WgSArV7~'
        'aF|6RCXt9tf`}<3VhV|vMj}#3L<WhNL?Y%A;cym-$RZI3k%&noVhD+tMIv$uA`T)EQ%FPxiQtfkc_d;QiO3=mDJ0?;60v|p%pehy'
        'NJIvSIEzG_OoYP)Bw`kcm_j15NJJWm5Rr&;NJJiqcmatxf<!!rM9d-)dy$A75|K#|!66YE5|KqBR*(oDiI_$r?jR92k%$c>f+7*C'
        'NW{gM2rVWe9}_Vj6OlzCU`8Sm9gFs?jh=P0XWi*pcYD^op7pS2J?dGHd)AZK>eA7%%5kt5z%hVh07n9joepcCaR@WL^$;ebDhe<6'
        'k67lOb;L54IAWQ`BbMbAM(0Y0&KORYetM}l#HotCZa9|FteAS+@nEd0pF=A6trp~v=NxN|dYs3KVTZ}ic|B@!{T5uqfWnQJb2;wm'
        '&$qk(BE(&HjE4DP?`|g(<?>~_x_KJQlC3?*Xu9=ID$5ylySc_08<xvT9NWX&WxMTlZtu|bD(Y3#4|cnsXnW?|m;2;ax%jw_HUEC@'
        '>h|lt=f*XW+v(F-bc|~5gM^#a{&S++ZP(m0Kj8G52yVAEi+a132g8u-@2fomsr_d7f7!K6<9}fK|28hQpFxJzxv2ddtlhRIKTUVG'
        'CPT?+)0xJ#&xYeHElfiZe8ok*2$d{gQ@`*ZvK^p>`6U1V'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
