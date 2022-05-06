# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/reg/udral/service/battery/Error.0.1.dsdl
#
# Generated at:  2022-05-06 20:25:55.367929 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.service.battery.Error
# Version:       0.1
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
class Error_0_1:
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
    NONE:              int = 0
    BAD_BATTERY:       int = 10
    NEEDS_SERVICE:     int = 11
    BMS_ERROR:         int = 20
    CONFIGURATION:     int = 30
    OVERDISCHARGE:     int = 50
    OVERLOAD:          int = 51
    CELL_OVERVOLTAGE:  int = 60
    CELL_UNDERVOLTAGE: int = 61
    CELL_COUNT:        int = 62
    TEMPERATURE_HOT:   int = 100
    TEMPERATURE_COLD:  int = 101

    def __init__(self,
                 value: None | int | _np_.uint8 = None) -> None:
        """
        reg.udral.service.battery.Error.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint8 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated uint8 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 255:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 255]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_u8(max(min(self.value, 255), 0))
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8, \
            'Bad serialization of reg.udral.service.battery.Error.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Error_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_u8()
        self = Error_0_1(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
            'Bad deserialization of reg.udral.service.battery.Error.0.1'
        assert isinstance(self, Error_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'reg.udral.service.battery.Error.0.1({_o_0_})'

    _EXTENT_BYTES_ = 1

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8Q-pP50{@j)-ESL35Kn2-rtW8ysuCdR76D4saBf;!B>I3H$7!P^cCekONTAc+-PpV8-R-fv=f+5ts1P5OPJrm~zynV_@E`D3'
        '@WOw@%=sfu(g>Uv-`(!c{$}PkGrxR&=GVV2&J=&yjieu#Aaq;<TJlhS#k~+5*H=-ZjI@wvms(b*zD+f>`w8SP^QGtcvwSg|bz>gk'
        '`V9?TCk-?Y9kkJtJ~$q?7IfdKX{~gg&AC0$Myfa$GugSl;q%LUb7u3@clq-?yWrvhExpu&$-h9`C!iYd%Cp&Z31M)6rsM|Pa@P{X'
        'la41^M$*b2?pWB3jqJt{Y{VA2pbxut!S$qdLx{Up<ePJ7+~>x+kqRIe*Rtz7BSUn|sp8r;Es;mx=FL32<{Hc6fa_q=&=096X0zEI'
        '4^u>N#toF8XEQl|y`0TeRZM5>7=&05*N0E9Z_bG~#M|P=z`~h&qh8C!&1}A|bi_lZ642aYOr1PC>kjR|HHrc3CmIZe{7?kun#B<w'
        'j&2mUvhy9yefnx}eSP?h>)EN>IXPxL1n};E;k&R}S#wt_?RKsC8Nu9Z3t&S^Fe6kN1}s*VdB9Qw0poE$QW_k#1{R7dnXi$0m^#Ka'
        'Fc~EwL=f8o@CN~OBqq*5z`_|K7k9JQR;Iytsa~tCwcJ*%xwla*g1Iz_Qp1<2#HcaV>4bP2i?~Fh#5_iJAG>&Eii^*$ZnxZ8v)O1C'
        'p{c}-3~S5-1F9B$Wp)Bd#ADtqyl19wEJVvi>@<YjV(hFsv|CyOVdogaJ5z<G+NiH@Jlt(o+8d2Jp{z`Vri}Q@F|xfpEOzFrxFfsi'
        'fPqXJ7D;4V++~F`$VPcQS9hlZ)Yz*v*EU+!N0sKoB3C<;xxyO*X?($T7X#u!U&TQYlmMv2SxA&O$g%)~*=K_HkW#UqYK_|i9$|Qo'
        ';k!2tzB$6T)u^lyv`+}y01O3SjErG?fWf{G5SRj<;T;&2E=Fqr^Ei@e$aS?^+uCvo&R%1yT`7Vk-Z^6N{xrVL7Z!KxYm+9k5BF4P'
        'IeFM&DlUE|S?EI;nz64G{8poK%(MH`cvdQKR2#eXHUR*NvPmPlnQmjf0U$$c=y1(CT15pWt1OmQ!u=<sJx+-ZTY=>*6t*Hf@jpAv'
        '{X0`2zS6F3@6@n}cAGW#QKS8eRGeP9JxwmIPFk!swhF%8t5_BSPM{(YMJ&)E?x`M>JqXp)K@=b=h=xP_Rk=VQ2g!hJVPYJ+UVkv>'
        '2@n(WVoAIw9*B>`x>yyTif!?^cr3cY7h1&Pndpn}#W&&?@uT=%{3iYsf224}1HcL7Q@_ezWS8BJ+=swTl(w!6@_IJ!8kK4va3KUY'
        ';W#R@bMzBRFVD{JpbpvJp|3A-G@mNt=oE^C$61TN97omZuCzH)q@M^Lu0f>o?9C+gLg~AxP12%M9>@bafS*x96ru(18g?>#8ZtP~'
        'E*H|px$UetG(~euV|~FD+#o=WOmRntUWl8IcV3&Bc?dC1EPvR=ee941yEJ)8U8z4P`C-dUwCc$Kv{S<VKWzIGyPpae3;|zZlQIc5'
        'H0ls|F(v}>9V)FOZ3Mw_wum`iVjLUefXSo#dk_aoKPVXhCag`&$K^7_&QtkBCJ;#ODBUg7Te*c+-LX}dtRh&$LPd8_Hyt~Q;6|OF'
        'ga*cD`H-^$cxc6u!C!A|Z`3PWPN}p}^bX`Djru4Jt;AY9YW#@lNFm=1^ynDTerOx*j$-JrqC?OYY5UlTG1}-z>EvQ(t6b9-W)kpG'
        'G>$X??KI06>OqQ77~_{<FnYVFqzG9DfuJ&=PX%y;DO3hZ!~!~IP^E>Kw?%Ne&N7?OM+~)flo)ojw3i%Gh+c?feSak64x}WK&mMix'
        'vx}?JZWZq>80*OFG^R1n*hxlAKk^h-3bK0}D+i@AMWs<>9<}>e5}$Q_AyIIPzq2blJRm|I+a&&>)p{C+T=$Qzid#SBi<@&l8xQ{<'
        'NCp;ATc;lS8OfMrHa_rudN@Z?8|#+vmq@_!xcHZ$o_f@woPPl>F`mJ}3;+N'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
