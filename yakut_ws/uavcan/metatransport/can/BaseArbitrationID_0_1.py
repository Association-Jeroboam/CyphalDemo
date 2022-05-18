# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/metatransport/can/BaseArbitrationID.0.1.dsdl
#
# Generated at:  2022-05-18 08:59:55.963672 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.metatransport.can.BaseArbitrationID
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
class BaseArbitrationID_0_1:
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
                 value: None | int | _np_.uint16 = None) -> None:
        """
        uavcan.metatransport.can.BaseArbitrationID.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: truncated uint11 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        truncated uint11 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint16) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 2047:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 2047]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(self.value, 11)
        _ser_.skip_bits(21)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.metatransport.can.BaseArbitrationID.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> BaseArbitrationID_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_unsigned(11)
        # Temporary _f1_ holds the value of ""
        _des_.skip_bits(21)
        self = BaseArbitrationID_0_1(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.metatransport.can.BaseArbitrationID.0.1'
        assert isinstance(self, BaseArbitrationID_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.metatransport.can.BaseArbitrationID.0.1({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8i?xJe0{?YWTTfF#5H3Qw6(LwK5g#l(7&P%HKS3Y{JOYg<Z)UT5cIa+$ZrR<_v?eC<pb5z&ny~%~|D>}NXtB_wIlFWDcIKOJ'
        'zEA!6J5{^<;j^+YtxO|k!Dyc9uUw=Mv82e#!fFQ|A09hXC9X2?sb7M>@Gs8%H@}H>mh+7KFDu?ncphcoxHCMrWno+tEZf||TO%}C'
        'oi6hIU5~S@3&zsLs~XOnT%9j`T#F}u`ZJFW#+@@-R1U2FLeJb&;7ydr`a2D&92PduBzK&-Q0;x`rO}yox=Rtw&$-o|9OQoPpabT1'
        'mkmbsvlQ}<Q$B7Gc*3n?Ss}rz6@1*j1`27>4*3p(i#nS4;Xis@Vb<|nawA89&MTqnSnu+*q6(&%EE113Pu4|TXmcrb-nreCYU0}6'
        't#k`5iP#hRjFzsR#H*HGQ5$MqZBzoVIYKQH{lWMsu%(tQ^(mn=kZ=dmpW`As)jg0b%#soQAucmpR3-s(q`*o}UEoakq*{2KYm-`f'
        '?O?qi)+Sz4SE>l|cu;DO^E>@g@pKom!sFAj5~)s@flif%_lEPb9;XL#BHi5*l*h?S>)M#8qBqf26o~OI5Z+{pTdL1M?gCR?oq#`A'
        '>-cDE>lLN7v?Px{)nKAPy-4ZN=hxH@XGFQ~|GUS9ZS6i>-jC^eMKw;cqV(9h55)E}QBcQJ+yOB_gA0`(l|U^NW~jAkmMBd#S9`d0'
        'C4#Xab)eqgoc3^ar^v(1@;f1MZh%N!gk2iRJQ~4RI;_%^oBmk#G#d!?m*0#VzpbF{EeB<hx+_8CWjYT_K?mLohncV#G}Mqi&!AV*'
        '^umH4lCs%AmLj075*m;?A#SNt`gh2oLy(MTt8udxm5BZU!KjKDwgdnG'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
