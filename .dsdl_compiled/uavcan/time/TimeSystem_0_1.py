# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/time/TimeSystem.0.1.dsdl
#
# Generated at:  2022-05-18 08:39:29.090545 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.time.TimeSystem
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
class TimeSystem_0_1:
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
    MONOTONIC_SINCE_BOOT: int = 0
    TAI:                  int = 1
    APPLICATION_SPECIFIC: int = 15

    def __init__(self,
                 value: None | int | _np_.uint8 = None) -> None:
        """
        uavcan.time.TimeSystem.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: truncated uint4 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        truncated uint4 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 15:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 15]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(self.value, 4)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8, \
            'Bad serialization of uavcan.time.TimeSystem.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> TimeSystem_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_unsigned(4)
        self = TimeSystem_0_1(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
            'Bad deserialization of uavcan.time.TimeSystem.0.1'
        assert isinstance(self, TimeSystem_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.time.TimeSystem.0.1({_o_0_})'

    _EXTENT_BYTES_ = 1

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8!LWp40{@j&-)kF35S9}=c9b?H*ckeYY@uz^7N6yZ5R%ddM~PdZSQ3$1N}()!cO&iAce}^#o^2Hh%|i=@EiHKaFZI3uQD^V;'
        '!*=jPg^>1kcILkMX6D;pSO5NZy-|JK{bHJ$G>fPKEm$UgW^o1)O;lbeBP@9L_R#7wv89I5v;cqZKYQ(e@ekb^l`Kd5cFB$tCL=3y'
        'h(`D`oEi(ccN_E=v=K^r-f-*R&DQ6>+vu+R?q7R%hcaumh)WB`|A-;40kb&e-P(bGEM0<V(v(?7Z9sONd!a=xtT@IKo8L+!CKA$)'
        'v@ijEIiou?7M5lpCzku}Dh5xOu{2jHc)sPf2lGI|Eo!6fFqkl-mEZg;@3yG1Or}hy7XzJ@F<*0Q$1E!m!75Ev;$6ez?p?RhRx<e5'
        '1qi;$w`Z$&yQ};?{z119g7f=zoUOxtuRrSdI&C`a^x7}zvwnZ%`9}^8l~h(qk&sXcVuVb9#7fzydBr3QVf9MG7&L@~mNQFI1x7xw'
        'B;ia>(8??jrAf|?fMmc56M1)w&NBIM&NiGD8cZneC9XGKF^hXFo9D)N-0iVuN!T@LKbWo2?p9hpWNBhd^5bim_<YX6&Cz}bQ~v&+'
        'l|~~JQp?$!$i7uMW*NHhOTw)!%+uXnkkN@a5(T7!MM_V0!_)31M_N15;21SW94dOSGI>F&bV;J5WkMPx3WzN87&K91f=*f)Kx=9U'
        'WJnRDGwS!AJZ|l@_V7DuwVqbr9|$7H`1_rz2H6RlhEj~hDSC;zB`*Y@$7LK?8aBQj3@cz!vz{?im#s9gFcB6aF6(NzDzh}e$6>Vf'
        'd8+~r5>E+BQz0i+PBn;BjAx!va}g4;V*e0R7KPFlPmQrDG%$m846rb`5r{`77%}i+7I7@8WCTeL?=dsfI3$D>MJAGpe{3th!&|c^'
        ';g8(P-v8)^t^L8^Wv9JA>hybbIC#<S9CX@YA|CHAU$J8fNW^$C92Jm&y_82%ok&t>RUknE-T-rB@6iGcxXlZiMdN9$fdLia_xKn5'
        '6aE!{!oT6qOH`8-a4_)wkoq%smsSkZKp_>W@40)_s8T0@h74%IP%GSe_{&7>-R%JqcRC2W=cr99yQm#p1;M>h2=AKhX~9|c9CGE|'
        '`$ZXJrc}eE%)<MYs)&Pjs}^YV54ocVE=4+OMSD@0VsC?hZBot*A_;{HB6=(m@MlQnAEOJb0d^?piq_?<%#8*?Wh92Grwo!)HA~pb'
        'Q7`chz&@{M2<(Z{M^Uqbdc$OBF!ZXGCnYBwIk|W)G@&kKXrm~oXq;hYpUx#{DYppQUVZlNt!Ki%te%Ik&{}tss=_;RT@W+PV}-OL'
        'FNa7oUMC^tei3q4dU<W!q6wl+J^#tQGpHx(jYC`oYp={Qrl(h}eCJR9u)F$~iSf=X>IlBOQO1~OE+j6)f}MuNdbp0T$N_&dNH3Gs'
        'wc0D=(4f(OW&1qX+y?*v'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
