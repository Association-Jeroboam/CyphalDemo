# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/physics/time/TAI64Var.0.1.dsdl
#
# Generated at:  2022-05-18 08:58:47.426797 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.time.TAI64Var
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.physics.time


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class TAI64Var_0_1:
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
                 value:          None | reg.udral.physics.time.TAI64_0_1 = None,
                 error_variance: None | int | float | _np_.float32 = None) -> None:
        """
        reg.udral.physics.time.TAI64Var.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value:          reg.udral.physics.time.TAI64.0.1 value
        :param error_variance: saturated float32 error_variance
        """
        self._value:          reg.udral.physics.time.TAI64_0_1
        self._error_variance: float

        if value is None:
            self.value = reg.udral.physics.time.TAI64_0_1()
        elif isinstance(value, reg.udral.physics.time.TAI64_0_1):
            self.value = value
        else:
            raise ValueError(f'value: expected reg.udral.physics.time.TAI64_0_1 '
                             f'got {type(value).__name__}')

        self.error_variance = error_variance if error_variance is not None else 0.0  # type: ignore

    @property
    def value(self) -> reg.udral.physics.time.TAI64_0_1:
        """
        reg.udral.physics.time.TAI64.0.1 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: reg.udral.physics.time.TAI64_0_1) -> None:
        if isinstance(x, reg.udral.physics.time.TAI64_0_1):
            self._value = x
        else:
            raise ValueError(f'value: expected reg.udral.physics.time.TAI64_0_1 got {type(x).__name__}')

    @property
    def error_variance(self) -> float:
        """
        saturated float32 error_variance
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._error_variance

    @error_variance.setter
    def error_variance(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._error_variance = x
        else:
            raise ValueError(f'error_variance: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.value._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.error_variance):
            if self.error_variance > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.error_variance < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.error_variance)
        else:
            _ser_.add_aligned_f32(self.error_variance)
        _ser_.pad_to_alignment(8)
        assert 96 <= (_ser_.current_bit_length - _base_offset_) <= 96, \
            'Bad serialization of reg.udral.physics.time.TAI64Var.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> TAI64Var_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.physics.time.TAI64_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "error_variance"
        _f1_ = _des_.fetch_aligned_f32()
        self = TAI64Var_0_1(
            value=_f0_,
            error_variance=_f1_)
        _des_.pad_to_alignment(8)
        assert 96 <= (_des_.consumed_bit_length - _base_offset_) <= 96, \
            'Bad deserialization of reg.udral.physics.time.TAI64Var.0.1'
        assert isinstance(self, TAI64Var_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
            'error_variance=%s' % self.error_variance,
        ])
        return f'reg.udral.physics.time.TAI64Var.0.1({_o_0_})'

    _EXTENT_BYTES_ = 12

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8N411v0{@*>-)~bl6fQqX+rZc=wmob}czb|WYj2Y@ZPW6wcCa$YDBW5i1}Ycddrx9(H}=K$EzKmP@vsRbOGCoj-?Tq#$4=6;'
        '6eev^qWId!$DhCRopbK5XaBra84DkKrRZfk%cEF>;xy;K&?JW_PGz@{nj3KTgB_#F)RYQ#dj+^RZuW(H?q=+GENB<kuPEq5Wu|Bz'
        '6|ARusw2a@5bbW<UT)l{%Gt?yAC%@&I5uV{?hnRqTx+a#>Ua0T+4C_qM)9OHpxqw&eh;ccD`&?yIpo<0O(o8#p|SB0+3Efy8@HGL'
        '4V+^WY-$LCUD$K%qrt{Y??X^1-sOhxBZBE2-Vu=976v+?j&pN9PPmD45FNu@YaP+0RGYXfGemdUe!4w$<F`dOaP6*N@|67MesuQZ'
        'SQ{!bs<NYwUX}@7>71c_xgnfA8)q_gcKwl{LTX5*$o9zA;aC&MX`vw_nu`=jZFQwOU#;PHw_05b--iTwh+LUad+A6B;-uG)?Q_Rw'
        '*k>BAlR=>%r3Nzh%3h4y`~b4Jkjlh7b6a*g*0NM7;6e^@K@qH-@P9c^oSoW6DIIM4**8eesRhK&q}R^rf;(He(JL6uZ$ei(`*~3&'
        'IZtDZTbcXwMsd~7p22C1eF&&Op&wFo=Y#6(#Sqr08r32nJZC(YmtsaWVp1TCkLEs4!M$R$5B@qcHnuaMnS`BN#QPyRO&}*T%$P#2'
        'Ei9xe>J^cZ3wRmiej)H5G1JXwBl1Hj4Uo2yU1AuJJ`HP?3h^FEh@vKKsmLyL3r#kR?DD525HA}gsKHF2`CQnWmdax!{OA%<K=b(k'
        'Ybc2bo!=ACKOlsfa7{93bCe^YIylQp6+95xCabm8`to9JWu;0ARI@}xIP0wx&3NA|m3X)=&>0sUJiy3cU=$Tt2E0WA<{5zKPd}4{'
        'VMvreljN`u`JvB_k|jbyv`EZgE(OiYE}?k)Xh03kwIsTLl(#u(LXkt1oZq0J4M;=^5!oyiZdWAZIxV#x+$Zb`)SyE6J~us2fGmyX'
        '8F=hI5UDH%$9r;QT6U4!$OmSlAM8Pxag~a|IcD+UC961@k@{ma3vd*&;yIxNg=Bb&+EhdG17w5~3JV$31ETvIF&Z++!GGohv?Fm#'
        'pu>gmzTtqTChz$p>u9IRFo_dD^+4D-vc@BQI(t`h1K)&jWX4}-bO+4)ywq4`hPSEXIfJR|M5_OQOQTV6FvLaMsM7xfD|k79Y;lAv'
        's`%QL<e1l2hgEn~1u=!q+t1Ek_=cPB!}AV44(hNy6U)L`@;)cJ*G(iA8>|s`vG`z(_d>sivPPk*Q8hmor;KB>Vc*#gw`t}x<b)Bs'
        '>sPnR9EH()dlfzG)4T-thns1wzt#!1#G>!WwI<61uiNFqHwqlk13#GX%>q@1yIYff+t_Q3Z3GSqpODx-x5`8(p&^X-eY06RhNXPe'
        '!?4jzZRV1iW4(!e(IV_ic9mUwiT=8@Be*HC_t+^+z|<3fyiaZp#<<O1TWnP8&H7?vd3mw9RBtwyR-3ijO0`jIE;gEtrP}gpeW}r?'
        'I^VhiqKlX?QsJGkbz&ZSXn#NI3+Hitukx*5CBxM@6vI$=`e})EI-48TjZpVM;~y52sB&9iy$R`#Wy*IWU+btjX^Qg1oDtHH9vDLR'
        'DbGXyu593>m=CWuUVMSMcX@+j5WRd$@w1T6gzuKXzVbxIY?=v1OE&+CMO$ov)o0iuYp^A@%vM;Ft+F+C-A)hRgO0Z)_BFO3_JnP)'
        'n;|aj7Q1t(q<e>>J4e*@$qgwyOz}>c+Nr)uv2yxXsCRm6u?MYF7@?n9>+B)^9^tu<QAlj3kKw)-8bN)6_C`<8=*h_FftTuuX)nU)'
        'ANLbOXHp6P00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
