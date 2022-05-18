# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/pnp/cluster/Entry.1.0.dsdl
#
# Generated at:  2022-05-06 20:35:05.943051 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.pnp.cluster.Entry
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.node


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Entry_1_0:
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
                 term:      None | int | _np_.uint32 = None,
                 unique_id: None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray  = None,
                 node_id:   None | uavcan.node.ID_1_0 = None) -> None:
        """
        uavcan.pnp.cluster.Entry.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param term:      saturated uint32 term
        :param unique_id: saturated uint8[16] unique_id
        :param node_id:   uavcan.node.ID.1.0 node_id
        """
        self._term:      int
        self._unique_id: _NDArray_[_np_.uint8]
        self._node_id:   uavcan.node.ID_1_0

        self.term = term if term is not None else 0  # type: ignore

        if unique_id is None:
            self.unique_id = _np_.zeros(16, _np_.uint8)
        else:
            if isinstance(unique_id, (bytes, bytearray)) and len(unique_id) == 16:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._unique_id = _np_.frombuffer(unique_id, _np_.uint8)  # type: ignore
            elif isinstance(unique_id, _np_.ndarray) and unique_id.dtype == _np_.uint8 and unique_id.ndim == 1 and unique_id.size == 16:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._unique_id = unique_id
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                unique_id = _np_.array(unique_id, _np_.uint8).flatten()
                if not unique_id.size == 16:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'unique_id: invalid array length: not {unique_id.size} == 16')
                self._unique_id = unique_id
            assert isinstance(self._unique_id, _np_.ndarray)
            assert self._unique_id.dtype == _np_.uint8  # type: ignore
            assert self._unique_id.ndim == 1
            assert len(self._unique_id) == 16

        if node_id is None:
            self.node_id = uavcan.node.ID_1_0()
        elif isinstance(node_id, uavcan.node.ID_1_0):
            self.node_id = node_id
        else:
            raise ValueError(f'node_id: expected uavcan.node.ID_1_0 '
                             f'got {type(node_id).__name__}')

    @property
    def term(self) -> int:
        """
        saturated uint32 term
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._term

    @term.setter
    def term(self, x: int | _np_.uint32) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 4294967295:
            self._term = x
        else:
            raise ValueError(f'term: value {x} is not in [0, 4294967295]')

    @property
    def unique_id(self) -> _NDArray_[_np_.uint8]:
        """
        saturated uint8[16] unique_id
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray ) -> None:
        if isinstance(x, (bytes, bytearray)) and len(x) == 16:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._unique_id = _np_.frombuffer(x, _np_.uint8)  # type: ignore
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size == 16:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._unique_id = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size == 16:  # Length cannot be checked before casting and flattening
                raise ValueError(f'unique_id: invalid array length: not {x.size} == 16')
            self._unique_id = x
        assert isinstance(self._unique_id, _np_.ndarray)
        assert self._unique_id.dtype == _np_.uint8  # type: ignore
        assert self._unique_id.ndim == 1
        assert len(self._unique_id) == 16

    @property
    def node_id(self) -> uavcan.node.ID_1_0:
        """
        uavcan.node.ID.1.0 node_id
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._node_id

    @node_id.setter
    def node_id(self, x: uavcan.node.ID_1_0) -> None:
        if isinstance(x, uavcan.node.ID_1_0):
            self._node_id = x
        else:
            raise ValueError(f'node_id: expected uavcan.node.ID_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_u32(max(min(self.term, 4294967295), 0))
        assert len(self.unique_id) == 16, 'self.unique_id: saturated uint8[16]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.unique_id)
        _ser_.pad_to_alignment(8)
        self.node_id._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 176 <= (_ser_.current_bit_length - _base_offset_) <= 176, \
            'Bad serialization of uavcan.pnp.cluster.Entry.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Entry_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "term"
        _f0_ = _des_.fetch_aligned_u32()
        # Temporary _f1_ holds the value of "unique_id"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, 16)
        assert len(_f1_) == 16, 'saturated uint8[16]'
        # Temporary _f2_ holds the value of "node_id"
        _des_.pad_to_alignment(8)
        _f2_ = uavcan.node.ID_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = Entry_1_0(
            term=_f0_,
            unique_id=_f1_,
            node_id=_f2_)
        _des_.pad_to_alignment(8)
        assert 176 <= (_des_.consumed_bit_length - _base_offset_) <= 176, \
            'Bad deserialization of uavcan.pnp.cluster.Entry.1.0'
        assert isinstance(self, Entry_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'term=%s' % self.term,
            'unique_id=%s' % _np_.array2string(self.unique_id, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
            'node_id=%s' % self.node_id,
        ])
        return f'uavcan.pnp.cluster.Entry.1.0({_o_0_})'

    _EXTENT_BYTES_ = 22

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8d4_dj0{?xNTW=gi7RNol+eyqx?1Yd&(p)xc*rg#X7ccj0yxByxF;=*U7u2emu5nf9>F(`|<3U0S4~r7i5+$XO^2ig4ctZPt'
        'B0yrV655BA_6a@$AA!d`XXaFF5AjBd{-<uI&Z(OIo$}SmPYy4P4gNJJ^L|{$Nf?!?FfuXk$#$Z`sFU^btTdH!&4JgeqV806q2B1{'
        '%H42}e&F7B%gt1j${vm%t>tD%reU7uVJE4}N)_Sn)2isZW;WVXMQO6s>9J<!Ew*ns(Gp`Hx({5lFOpSNn08&M(!GOD_Xy|CEZ0n('
        'Gb)L<!<dg^S;?rP*!EhU7p7+_vxzen-%Lxhk*fGYTB!|H?9ORl)HYR=sC1*!P6X(@Bg-o4WwCO4sX4Ol9nrGzERJ2IA<Ss(&+d|I'
        'mZGwfX)KF)r=x3iTTeBUcrZQJOh$3man152)m24MWkID?a7lKnAeTAzbh9E*TX`Z=S>b7g4j02PJiXW)-{X9WLgINZoikf1{^MZR'
        'Gt{*^y91F*R8OVV@U-+1c6*<g)yMP+eG&t0<}l@4c1+cG0x;TkQo81p-*!7IjG!8AyJr9IOf}s9b!_s^%|w*tt_k*XQucf8EHQX0'
        'ix*Wd!=xzl*YGrCl@;6ZPe&bX@b2|9&7n&wSCzT@yz%H=j9ovE^X^%zlSCH%(MjlQQzo@?AG>8SYs)rfJ{k2)>cmwt<Q5q-bn|s0'
        '$*XA5)G;f@Stm%xt(fHY6zPN&)7(G9I?Lm8+@2q9DfW@hSh1hm2T1o>vB2~0;eO!t2TA9wIK<<NqzhIo@w~&_e}wdq759=Ju;M6>'
        '-^cMCBRy)xandC#?k5E+9w6Os#R;B&l62CFfcJlp^Z_d#B0Xls!=(3G@d*3*1?fR6PH|kn<b0Od-=m~cRy@XW{)+T5D}GJ7Y{lcG'
        'r>qD`AF<*I(ub^gk~Fa5H0cQ|o+7>9ir;V?Pjf!ckRGw(S&rv9K8F>~@3$P+^PJ}kr1Mt1$nm{II&H<vocAjn=c}CmdD0at-sX5U'
        '@4Ln8uaRE0;wI}Y*4wP#vHrmNBkNB?y*S%q<ES^5y|Lnr^WJ#d8`>LN-nizCo8GwPjoaS%&Ko~?<414&#72$qLk`Jwz-;bo(}#jA'
        'o2ygvr&>h@KgI`}@XbN%@e8X#)<vF~GLT7<bq1gD3&DG;$O6+1>h#?-yD~yFJ<irtv%rNUMWluoR-K;FbG}mO{qMLPi?+!HcgTev'
        'riR}%hBSto$Yyazd5PNnVZnOe=`ZzPN@RVk@<L&hDt6bKg{VvLjPk6gD6h5VU{q#x(NQ>%s3@06@@9r4F>Tk(tz&)MTBqI{$eh*_'
        'h<2S(K^)JGYv#}Pb1joq<e5Wi*KOomRHzN43GTODvk<P+!@O}lWsXJh!fJRrd@>|hx{AumVx(n>5fsF3B>$%AD0dyx{B~7!O{(y`'
        '16qqW5YE4W^#u84dUY?r^DuERIF$fz1rt_jj81|q9n_r~TSd}0=|)f$c-54AkjOrk@cFlBRT(7N6{=HOrori_RsxIxFZYV<m+YMC'
        '72fvt`ZAo~Rolv3bxhX`e+`4_y$qe0w3~%ahx+v3F7?y;Ilj~Zx7TGHV^}|fJC2?iE?6CY*JT@@8ToLw6SMd`IEO!qKj8oKds4eK'
        'LhTk)dvXtI&oH&8nc7oK?MbHg#0a%pBh&__HZZk;sSQkRU}^(X8<^U_)CQ(DFtuTX+Q8HXrZzCOfvF8lZD48xQyZAtz|;n&HZZk;'
        'sSQkRU}^(X8<^U_)CQ(DFtvfH4NPrdY6DXnnA*V92BtQQP#c)qz|;n&HZZk;sSQkRU}^(X8<^U_)CQ(DFtvfH4NPrdY6DXnnA*V9'
        '2BtQ6YJ;aXcxr>EHh5}-r#5(MgQqrlYJ;aXcxr>EHh5}-r#5(MgQqswT7SldNA(PWfkAzIZ3v0GV4A3`^lkdW0)0^5(hpyLwly}U'
        'Kd<#y*Y($H`WyZ2vi__7oBq50hyJJjS2KYRegq;v`CYRxc=Yckm;N_V>Z8|E6|AT0o>4ot4b)%}LJOlI9ulS`K82A(gCO~B+{w~X'
        'rDaVaZ)An3bT16n6D3O(6gz1%@Np(5&QUxD2}a0?RV7VQ?ggCx-m!K<=<wMrrSg#8^*u^2WqOVxl<7~G|L^Vcc|6QP<FY_&ulYOC'
        '79iU6_o6i*T7X0gh-mt=HSAbXCG~!ay`OIPe$V(D>Hg1f@)y|q#m^`2?xr72_&<_=lxiRj000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)