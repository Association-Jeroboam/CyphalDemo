# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/reg/udral/physics/optics/HighColor.0.1.dsdl
#
# Generated at:  2022-05-06 20:25:55.127649 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.optics.HighColor
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
class HighColor_0_1:
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
    MAX_RED:   int = 31
    MAX_GREEN: int = 63
    MAX_BLUE:  int = 31

    def __init__(self,
                 red:   None | int | _np_.uint8 = None,
                 green: None | int | _np_.uint8 = None,
                 blue:  None | int | _np_.uint8 = None) -> None:
        """
        reg.udral.physics.optics.HighColor.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param red:   saturated uint5 red
        :param green: saturated uint6 green
        :param blue:  saturated uint5 blue
        """
        self._red:   int
        self._green: int
        self._blue:  int

        self.red = red if red is not None else 0  # type: ignore

        self.green = green if green is not None else 0  # type: ignore

        self.blue = blue if blue is not None else 0  # type: ignore

    @property
    def red(self) -> int:
        """
        saturated uint5 red
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._red

    @red.setter
    def red(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 31:
            self._red = x
        else:
            raise ValueError(f'red: value {x} is not in [0, 31]')

    @property
    def green(self) -> int:
        """
        saturated uint6 green
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._green

    @green.setter
    def green(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 63:
            self._green = x
        else:
            raise ValueError(f'green: value {x} is not in [0, 63]')

    @property
    def blue(self) -> int:
        """
        saturated uint5 blue
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._blue

    @blue.setter
    def blue(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 31:
            self._blue = x
        else:
            raise ValueError(f'blue: value {x} is not in [0, 31]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(max(min(self.red, 31), 0), 5)
        _ser_.add_unaligned_unsigned(max(min(self.green, 63), 0), 6)
        _ser_.add_unaligned_unsigned(max(min(self.blue, 31), 0), 5)
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
            'Bad serialization of reg.udral.physics.optics.HighColor.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> HighColor_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "red"
        _f0_ = _des_.fetch_aligned_unsigned(5)
        # Temporary _f1_ holds the value of "green"
        _f1_ = _des_.fetch_unaligned_unsigned(6)
        # Temporary _f2_ holds the value of "blue"
        _f2_ = _des_.fetch_unaligned_unsigned(5)
        self = HighColor_0_1(
            red=_f0_,
            green=_f1_,
            blue=_f2_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
            'Bad deserialization of reg.udral.physics.optics.HighColor.0.1'
        assert isinstance(self, HighColor_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'red=%s' % self.red,
            'green=%s' % self.green,
            'blue=%s' % self.blue,
        ])
        return f'reg.udral.physics.optics.HighColor.0.1({_o_0_})'

    _EXTENT_BYTES_ = 2

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8Q-pP50{?|oTW=gS6y7x1TsBZrQYrz0x<!ISB(p?G1FArR+zM<HqLiY(Aj>mzvbLD9N46))R;olFK#JsuOAJ4TU&rz6C7YxR'
        'E3L+JF5kKMJ7<2L`0JmkTJ>{xi%x3NETRUqV3~N%;tV31sJu`{Sn%%kCsvn<Ej4`KDZrom#h3ntUvPCQS&sVq8ro5rYL-O>?--Go'
        'NEJ3bz7}o1sWPR#o2EygjZo6_nw$EecRu&6T5IfA|I)iz%B<BQE-e`UBf^hJY+&VGeMdl+UL@3@DYJ~)kmV@%LW^8jafBB0Po)uU'
        '3F$Y|LL2nu>Sk#yEX_c+E%&WDf+x&anyVB%zwPeq_kn_2w28Xipb8cJ;t#yLO^szTWjY-OIxS;fcjFpT?<Q!f67OmrWpmxAe4gLw'
        'o!)Lu@^|?A{BGB!-qrxvynFoq2=n@|`9z$R(6_$nrZ<%g>DWPiqg|(Vzj{Uwwzn#8H%X6JfO7Bk`w1t71{1FDQa7g$m_-@O`XTt5'
        'n>o}h2~valo!%Ms?#Akh4_z`bhK&BN_L-2;ql4}3y(%ZZ#y{;v;Ger2>#P3_b*Z@N0JZV>>2@FKvoZ!ZKg2y6ce=a|-h|)cAMp?P'
        '5?|n}yveutmwb<ZTOvDBz&0ez;!U2qoAgkeKuQaxEfuNXbGN8brA`198PI~^-Mgvq$VBYj%s$T6$$pTYBiF{7$Of*$Fil!~GVIrQ'
        'TUhTJo1KEQYzuPb-Md8@XCk3EZ)FxDU+_IRpcrSO8pIH*JBo<d9Y*io9E@Z1NwgA$+w?Y2b)Ir&Fh>p2hH*I(3HVcf@7dW{tyVb@'
        'A&KQc`jjRs>&wV$@?d#=`2jh2v_TG)&Y2|(6-|jS<XEJjNm>H2iby4wODTd8Nh&}CIDE()VLL<}R^YtMnIzDG#i+rpEzHAa6J&HO'
        'ei8+wf<;QVo8he)3ZWHFqp^cv8kj+n1)vZ`Bo!5x2qU?YD&ZPiOEPq_B*73dkTAv>q@*-Lw!5X_os-bYrN%J_4V5s~!AT<BLrEzd'
        '3S1Y2nM#=hV)b(G7F8`xiCr{UG4=zu4w_^AD16vxkYT(p$O3MGW^dTY$E509b3k>Jgc)x33A;#|WHl^}IK#XAus@9#y9IB~UVZoO'
        'wGCk(SMN_?F#T?vs=_-m3dD5sSRvDp8oS6m+?}DH-xZ*l#brL&k&`sx0yi+v-5dKXO|h5PjJW1%aLV0VxQW8l$X7zTnJywSF?<7t'
        'Jnbvco_Dvvi&2)C)n1upOn0uv;cLJ7g;xD{6XS=e=w|L)V`Yr}&4mp69uMp!9Hzp~$9W6sHNy5|vif%I;X*kZLYqW1FfsqLHOtTO'
        '9~6HFqdx-hb@ADiOuD{vXf!wMJ6&EEhg}!_3x*gmO2r2N00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
