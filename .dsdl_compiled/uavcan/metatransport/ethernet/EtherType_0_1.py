# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/metatransport/ethernet/EtherType.0.1.dsdl
#
# Generated at:  2022-05-18 08:39:29.463548 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.metatransport.ethernet.EtherType
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class EtherType_0_1:
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
    IP_V4: int = 2048
    ARP:   int = 2054
    IP_V6: int = 34525

    def __init__(self,
                 value: None | int | _np_.uint16 = None) -> None:
        """
        uavcan.metatransport.ethernet.EtherType.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint16 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated uint16 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint16) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 65535:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 65535]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_u16(max(min(self.value, 65535), 0))
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
            'Bad serialization of uavcan.metatransport.ethernet.EtherType.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> EtherType_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_u16()
        self = EtherType_0_1(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
            'Bad deserialization of uavcan.metatransport.ethernet.EtherType.0.1'
        assert isinstance(self, EtherType_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.metatransport.ethernet.EtherType.0.1({_o_0_})'

    _EXTENT_BYTES_ = 2

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8!LWp40{@j%U2haO6b+C~LTDj02#Hn{gP=ep21pZB^{F8QDOyNZ3Gh}~p7GtiRz2g9?OA0jA(e+#MY7bYF+YR<*z3*gCP1UA'
        '^D@`I_PJl@_}AHYe|KiaU$|C}q?0=14y+Pd{UUM=881v(8>c+P@cEv%P2n30FGe-QgLwB%d>!wE4zEN>{@aZh7NW{Z@WNYBx!PEt'
        'fk&_v_-rc~<C|fD55YQRs)#dT{#9!q#O_S@)bH_44ClD;-m1Lu;Nnjd<Am&{r()<lRiNcjR*PH;FSs8EJmGq6RjIrh(uw7ll~aQX'
        '<aXs@&?Y(sJI8b7xrS=sF?N>-yb#Xw(nyGSDO~PNfYP;WlYGyUD^>Jc+>PN9cV1LdSa}@ik0!@X=nRE!D1%upO%cOPq}}sjVbfIU'
        'j-Muh%Xqo9u5_31OZ*zIwFuii{%S4ab-WSgcnf!RQZnq<7F_D^2L&(e3Qv1NPXgddINP_PNV|^wPg|S(VRrSw+IKOP;&KXk^S?4W'
        'v$5M7=YuPFuSLhz1hc;OKVZg%J^B}*&bMpptLsxF2+PL^!}HN0BNHOSi+C4r;rI9mpWqJ-jZy+Nq!1otd>hX5zS;-L6IZ#CaVK2l'
        '&NQ|Fa%kYSph1QC^wTPj;cSo8u-{9&2Skih_o+E(68%rtDu%_)QH?@BfzrhARo&!T72Lw0(J9^$C8@!4hjJlZeIOX>{6sP_d@&VG'
        '_8@zhrGZAD2(`>nI7-e!<rArgs(|<wuZQ=0Ez#KYDl1wlIVK#F&{srrmXFx>*47r=g@JMuJ&l@eG#-sre#8ibZEx&sWQ#9QIi~3h'
        'qra&%`Isw(*331z1J6wVSOky4GfHc`r6gDi<qgY$S<o<~GpuhcJ8V;ySf6WZ#y1nT9?65s@*l5b`0TOr&&KOLm}(=O;iis(odn`W'
        'Wo~E^)VJp}8Ipgh_Qx8iY-5jPKF14G^oU?TT<8fYRW<nJ5dNIJJB`-Djz0F{%AfI0cj+&e(;HVGBE;@OlT)3gs?yUzhS*QWe0n~J'
        '7b*Y6q*5Y4lG_e-l{lUK1MgrNH=P9l00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
