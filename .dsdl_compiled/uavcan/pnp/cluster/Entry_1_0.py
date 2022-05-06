# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/pnp/cluster/Entry.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.336059 UTC
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


def _restore_constant(encoded_string: str) -> object:
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

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{?xN-)|ko6~}$!-%esqViQ6F$p&a@el3JT<3fL>F=?zJ#tJ{g3tG*+JJ&N|@9wfc9A6})@X#u$R_aI@Bp!J}5l@JR'
        'Dr%8vp{<a3K<ZQe1pWjbd(ORQV*3(f$@-p|ojG&P%<kvRy*BaTsrj+NUvo0=$7P&^QK<?e6Z4*ICn}6OSuf8@Qz_RRe61?#PE{A`'
        '^?t70P51Z*?tQn^Oh&2f;q#-l-0a9S%+oyVBz0M-B78ZmioR=RqD@tlCQF?jYo_01`=%2uG4^Nofot|hvZ@Nxt}9i#x6$by;oKeN'
        'n#l`BCGmC`b5SfS8C4Y9Ueoi!^h{+oam2zKX=yf66|bh1+EB&roc2d;Q$>kNH!AH!fX+LztfF2PE2kHmBkSG~O$*QCvrF^{GaCDo'
        'yX>09sH|if%Oc+C=z87Olg$KfOwTnFQJi&LvvgT?RS{HKP-zuhmfb4IWsW`FtO(Rrp2$>IxLcva$uJC0FEq#Z*q@@1xZjHx%$AB@'
        '8LWDax^`!GFj9%?sk9pImOjF69~3kCm_DITVxY||rku-;srpU;M%zwG*PQmtZfAuNRHJRz9QcE&hU>qEO<uVfkFwk~!Cp?vey^P+'
        '26tuQlImrc6lMM@?uM+gVmtn+sG|*@y?&uNd|BnHGWQ<0FM0=K*DvC@`_}3tkwt%W5c=AbNv+&p-IAEGWg9b}h<YY<;u;xpi;QVH'
        '`8tv0RkUd6m=*h2$4U2DF~RLg(s3)MxPO{;hM&)Jdv3U-*iSlb#Q|;~B;9YtJdeAN`+?^lBAvD3Fh5@)ows6<$KB8UM@SD_@c`*T'
        'D~|H>2RXiDq(`kdPP%BtL!@BE!=wkSIKksjl1^9=@cO4nAGYEV(qmRUO8S5mkFlShksh+*G{^OG&S#1JJx)4l#S<LolcY~r@f7Kj'
        '6;G3%wjv~b%!+47AF<+D(!h!{q$jL+j`Sfbe!+1(&-uJSdc=xfay(~wAC@`4UvXS7a-J`d&ROwmj_)_5Q&#+z^Zp&j`Fqa)BI&Xf'
        'Z*jbu*WKdz*GaEg@e%7S*4wP#u-;+)p7n>JUYcpKanu`2-dOg=MQ^<24egCBZ(R4rN8Y&QjoaS%#v6CM@x3>GV53I(A%|o-U^e%)'
        '=|e%5&DN=Tw^otCkMUF!zA<P$y}A-)UF4Z51DPaQXYd)n6uhU3EHK@mPTxtht0P3y``DUn=DCohh}3X(#p!81>nnvm@V47AX`5Vd'
        'mt5#!a`;VSNMpE&Y!-Hum#Ezz7OeN3{+s^1MApYDFBC?pVt1pNkGcfUD9?(D@>**SMP*hO9fc1P73C61-b|AurtO;9b*ztD>(qM_'
        'nbUd((XKNph*K4+L~4$27)0XS`F^ftvVvrD$nUz1q>Bo*fn33rx2qRUm>TW?dZInR^0>MZo(Z1~37f8>0<#clSz;^&Q5<W)rs*hm'
        '0~7voMRiT8aOVS>i)Rtey^fUyNoIO=FTkBKaWL4Q0M7?gS80q+f-D_Wpc-36(l_ZwP!)LSv<*Qb`&i89-lSP&kYrb>VriKMXP#RQ'
        'Fa|v4tFm9RbE;f;?%VUraBf$XD|6K`T{C<y2E%(9Ix%TC3!M)2nZc>*=k-}W-T}eaWgKHzKf*jdJvW@NGW^2JHeNXL;b<pj@Qt{D'
        'ug4$p|KgtfZjJD}#r&SwgWuE4?<wZ@B=dWM`8__u@74&vf%y&0Z(x1{^Bb7o!2Aa0H!#0}`3=l(7~wZCzk&G;%x_?R1M?f0-@yC^'
        '<~K0Ef%y&0Z(x1{^Bb7o!2Aa0H!#0}`3=l(V15Jh8<^j~{08PXFu#HM4I}&p<~K0Ef%y&0Z(x1{^Bb7o!2Aa0H!#0}`3=l(V15Jh'
        '8<^j~{08PXFu#HM4W8fN`3;`m;Q0-n-{AQTp5Ng44W8fN`3;`m;Q0-n-{AQTp5Ng44Yt;wu;HOSO<-VTA72|n;vT>zJ}Z5jzOX<a'
        '(zo=ZSI)M^#`LGP{`(F6k2U>;{&GqGQ~yhUrN7qy*8kD}ZN~BPk8tGcziZ|PKLB>KOMgq8`pc`S3f9wgPpKUX2Wl`0v4!yv5eZZh'
        'uf<5BL703`?qq4H(z2$YH?qQ1x)%oPiISxXik-X}_&Apn=_nq93?t~os*)xt_d?G9?pixBbpQD*rBadJ^KMGFX1bapmg#5APkXzv'
        'irYD8TzLhpy~gi^TYzxWcSLKzv;dhF5YzN0YuK@@O6vU>dq3Xpy~6+;>Hcmw_%rPN?8k$5chhSV{vUR4x(O@}000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)