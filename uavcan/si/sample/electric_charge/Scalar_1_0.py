# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/sample/electric_charge/Scalar.1.0.dsdl
#
# Generated at:  2022-05-06 20:35:08.529951 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.electric_charge.Scalar
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.time


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Scalar_1_0:
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
                 timestamp: None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 coulomb:   None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.electric_charge.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param coulomb:   saturated float32 coulomb
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._coulomb:   float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.coulomb = coulomb if coulomb is not None else 0.0  # type: ignore

    @property
    def timestamp(self) -> uavcan.time.SynchronizedTimestamp_1_0:
        """
        uavcan.time.SynchronizedTimestamp.1.0 timestamp
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, x: uavcan.time.SynchronizedTimestamp_1_0) -> None:
        if isinstance(x, uavcan.time.SynchronizedTimestamp_1_0):
            self._timestamp = x
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 got {type(x).__name__}')

    @property
    def coulomb(self) -> float:
        """
        saturated float32 coulomb
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._coulomb

    @coulomb.setter
    def coulomb(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._coulomb = x
        else:
            raise ValueError(f'coulomb: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.coulomb):
            if self.coulomb > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.coulomb < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.coulomb)
        else:
            _ser_.add_aligned_f32(self.coulomb)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.electric_charge.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "coulomb"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            coulomb=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.electric_charge.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'coulomb=%s' % self.coulomb,
        ])
        return f'uavcan.si.sample.electric_charge.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8e1>&m0{?Ya>uw#l5td}@?rUT_j-5Dknp#q8ZFD>GaoRL><r+>IpBS;-3cYy2-K7o*?X4tN(g{$Y`O(4x7U%+IfjmMUA&(HC'
        'Mcbc2pCITH<Y#Agxkr*?3y{89ayT=bEA{7-e_uE~QvZ~1=YvQ`vFB^9B#Y%|EQq=1hgp(mS{iQ4(~pcQLQ^RIc#w1Z+%A4@|6~`+'
        'aX)1V?9Uf$H)N@&rKeev!)YG#&?p)Dp<t@dy+<L7nX=`Szsr@DS!%^dIr(cxKeu$0j{MbrZp&Gp88{dehHLu=(D4fEhFrEBzbAPd'
        '9a=TxN6awaps8Z4Srp^tb!ViJ3D`48L!q)%e#WE6u%HdtZN;RRZY>d~K)X2Sj?cZyj$Fw^8o3L0%sol9?58~XC^fv#)p1|V`hhfl'
        '%+tORmUh9)kZI#5Sp-(TSzdbB3c_RFChR@HEp*La?5DQ8;De26#8h-t&_NNv)n*eJs!a1ROCwvJ^rI}aTmKsy8F?%?NsA=lie%g5'
        '2$v>CFhc~}<s@fX^N47fhMedu;e;trp_m$w1U^$kWD5K>r}1V`s9Oi2nUa0jUXUL5Zq{7rU=lFR7m3s);@c8@LUOK_Sf0l+WCmjH'
        '5fl>^N}-(L5!6&@J_CUw0Vj(8v4GgX@okkQhtl;he6=u=fMHzSB%1S@Da=5w&f%gm?Zc|tm2kJ(6j^JZfm?uayDTm^T4^$p@?CTj'
        '{MnAPy~e)berIC|TtfC_1a|U}fsOCa%n-6fR-bk@j(Zl^S&$Wmtgd!DWWbryH_4ump};Muj?@f1a))fJ*D{Zs1-lE#9YyxCB91^2'
        'Xdt9WQyy}ynUe9KF#!^RNTY|=g4^I2Sc?(qfL0^2LL*nL9=4+bL=XnrKrr8z;IGs`9+OZ>Ew$HNW;2Fdkm1tiogP_8Gehp(T_lhR'
        'Dfm)>zK|(MiXumU-6FvNiWD{GY!GLxjxhuZT7p*_{<sYlNznX0Fl)i$7$c17){ps8&EBZk=7)|-I4m?dYKC!uq?k9D7U%<oyD0>Q'
        'fD^T6p%BiLQ=3_eWnzYPC+5U8M_s2~@s4<xj$l2B`KELxpY&+&li&2LSS)Y+maFVV)pfo>+|V04X||Voww&;5gKYU$+Z6bI4he_N'
        '>{v^f`n1kZ7Pt0@PB{%%4slh({yj&-emS~q(J~zr0War{^g%xuG>sN-u^_I9HL+AcLy0&jg>vGNJt)uk+j5^rJ_gE{k?ob|eVr95'
        '<ggKQKWES`%1MM+2DY4j2+e)}A+A1$_B8q)G!BtrHy_KTEoU|dImGHNPcmCx&5HmE*H^q>#HjDE!@?ydn#Ky}(O0&-_R{9+t$52G'
        'I?EbtXLG(_8jQm7_g#V70|>%DdQHKj27($eTcG|k1>FFhjCl)1&7fe-UZ!@I>Wa`ubk;Gel|rT%aje2XKo%EG52#zfp&s}UvM-><'
        'z^hpT4K8wuF<*lWBtds-yKr5DyTFsFC7tt7Zp$Ni4g+F`d)SME7+iFt&6C5{4VN}Ae%tcYFQoan{(i)VNnD=rv)q>CRYLS22{MQe'
        'c=Z9q%QeMMpc<LU)Zqx4fN2cnZ^iG+vkzH>z43cYg5hqjh+$k0UfdO(zu5)at#kl`JZ~geI#mR4&qSs;)_`F9NKE2rgKR;ebQI5x'
        'RCLVY3B<9Ao^;>ih@%yqaO;z9eahjqTc1IksOYTYKZQ6|(bI@0D|*K9pGBOl=sCB49&x;)uQ@q$h_6-j0^+%fUPL@o(MyP@D*8I&'
        'Ohqrd^KUr4SDc=!PR^T7-&=@RD|!v_N=4sBe50ZS@p474BfehIcMvaC^aqF+EBY?tg^K<Vajv2_oL%#X=PSD4>{~=UThSjmJAaIL'
        'x}rCoy-V)Cp0oQs#OaDIJNs7<Co8(@?y=_lvF`3u$Mr--H{88$IsbOu{cbmLr|&!biNl{d{J`PQ9DeBV=ML{X+;S)!?mK+u@C%1u'
        'I{eDv*ABmN_^re58hkJ{>WIrNvCtCTmbl*%TP-14V!tJxwZs=K@nuVV)e>K~#5XPRZA*OThyq@BFcDymU~6}40XBA+IMe3vy}4M9'
        ';NTj*GT|XOeGf*dIresh$wgptt%~_)AUI)tc*GR=Z2X{{Ut3>Z?XIq^Z)~h}JFDGp=XQ5x<<|20N_TC&yWUyZxV_q0UvDN$Gw|Sz'
        '5obvN%EiB7(ug~#;a}ps_^<d+AvO=h-JbZRxW6Di62B5ud@LS_UOA>=CQLMsdt07;;du`$%>(~<lNXN;P>FaVwwm_wJMnbbWx^r#'
        '^hoEq2m>4^TKdu!R!%n^42A~&Z}3uSzSyCoaMKv3eFDEJ=>2C87Wzk87=aeXH8O1h)7Bx=4tBHeEo0=o{{t>mkb*M}000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
