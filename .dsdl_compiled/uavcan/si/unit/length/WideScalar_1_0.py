# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/si/unit/length/WideScalar.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.532479 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.length.WideScalar
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_


def _restore_constant(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class WideScalar_1_0:
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
                 meter: None | int | float | _np_.float64 = None) -> None:
        """
        uavcan.si.unit.length.WideScalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param meter: saturated float64 meter
        """
        self._meter: float

        self.meter = meter if meter is not None else 0.0  # type: ignore

    @property
    def meter(self) -> float:
        """
        saturated float64 meter
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._meter

    @meter.setter
    def meter(self, x: int | float | _np_.float64) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        self._meter = float(x)  # Range check not required

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Saturation not required due to compatible native representation of "saturated float64"
        _ser_.add_aligned_f64(self.meter)
        _ser_.pad_to_alignment(8)
        assert 64 <= (_ser_.current_bit_length - _base_offset_) <= 64, \
            'Bad serialization of uavcan.si.unit.length.WideScalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> WideScalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "meter"
        _f0_ = _des_.fetch_aligned_f64()
        self = WideScalar_1_0(
            meter=_f0_)
        _des_.pad_to_alignment(8)
        assert 64 <= (_des_.consumed_bit_length - _base_offset_) <= 64, \
            'Bad deserialization of uavcan.si.unit.length.WideScalar.1.0'
        assert isinstance(self, WideScalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'meter=%s' % self.meter,
        ])
        return f'uavcan.si.unit.length.WideScalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 8

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{?YXOK%)S5MGn49ULHv9C6_QCvYx9zaO`VAamHnSQr5p)ase(?6fqyGn(mHd66QK1Bgg1f#l}@Qf)hI2=Yp+epJ<0'
        '^;Oq5zux_Oe?GhV#ZUWfJ=SeuMmKod`d@6>y24c5s_#Z0T#6r_hheJ1G`R1#y-Szr@vHPQ9mly@+ZEV9o9w2t>tgi9wDzHB-Fg|C'
        ';zwV*^UAh%Nb#Q8xMB3&IyJL+@WajiGA;HNv)|LJ6z>}w!r;p(xH0{lZma5FrxfQW-nI3vnnP3DU`@y+-WJ{ue&vJTfXDkMZD+%O'
        '3EelP59Yf3w0HuLl^ugwb+t>)qxkXJoA4Y~JO$hHYyujy-_my}J~Csl>)H<W+dzK+&dM&KGgF-tzZh&4fc^+=Il0*b#!q~2Hp5a&'
        'p(&<J2|_WKNMXi_WQ0nJC1R8dsTGn4R!+ELOl!fl(pWMn6v{C~AgK@{ic=*8;!1O_1SL`kB^8#KGsN;O<(N@Lm;iW238q9SrQwJb'
        'I4cGz;EyP$l4GHjK#&b1E(Pb9D1xLQj5CdpMpS7^AebQu$rMM5ffJ<~uyZy_r~ofQh-L~4u8`tfQ^-mvumy@hT@gVL!;DEF55-cb'
        'R$_%T)<kQiFyRPlM?_%7FkuRCg-W^kQ`yYpeC2|Jal32ku1awRw>BQVHCm?JUJvcd)O^uA9O21p*AK3;!PV(?{K&lU7p^vaHw5GB'
        'bQ&L;v73g<fuVJ#xA36xATO;i;W5uZBNu1+_7VnY?@P$tbXgSp0agodd}rxHiic0PePi3N-KtCRlYS~&Uzx!zr#5HajV=W2U&|@Q'
        '_eKwJSyFI$GfeSlC#wP%sK{fULY}@O)7TLz9NaqOx!?H8rPs}I^BDS3wt)Qk8&&M46CA_4=M+Eq%7<rH=W{sT=p)`ST@Px%4P@M|'
        '$_{8jCC`B-Xf99ox4j!|=!Tuj_D$7zP;T>0d~jy#+OL=Yb84Pt>*>@2&F#BZK-k!Ja_P@>ym<20Si<L}zXnQ+ds7K?SALxZ3>$lq'
        'HwRh7(CZw1Xxv3_*H>Sl)2STGsVx2h$<pY)5d{DM'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)