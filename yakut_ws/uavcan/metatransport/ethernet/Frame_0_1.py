# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/metatransport/ethernet/Frame.0.1.dsdl
#
# Generated at:  2022-05-18 08:59:56.247558 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.metatransport.ethernet.Frame
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.metatransport.ethernet


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Frame_0_1:
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
                 destination: None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray  = None,
                 source:      None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray  = None,
                 ethertype:   None | uavcan.metatransport.ethernet.EtherType_0_1 = None,
                 payload:     None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str = None) -> None:
        """
        uavcan.metatransport.ethernet.Frame.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param destination: saturated uint8[6] destination
        :param source:      saturated uint8[6] source
        :param ethertype:   uavcan.metatransport.ethernet.EtherType.0.1 ethertype
        :param payload:     saturated uint8[<=9216] payload
        """
        self._destination: _NDArray_[_np_.uint8]
        self._source:      _NDArray_[_np_.uint8]
        self._ethertype:   uavcan.metatransport.ethernet.EtherType_0_1
        self._payload:     _NDArray_[_np_.uint8]

        if destination is None:
            self.destination = _np_.zeros(6, _np_.uint8)
        else:
            if isinstance(destination, (bytes, bytearray)) and len(destination) == 6:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._destination = _np_.frombuffer(destination, _np_.uint8)  # type: ignore
            elif isinstance(destination, _np_.ndarray) and destination.dtype == _np_.uint8 and destination.ndim == 1 and destination.size == 6:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._destination = destination
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                destination = _np_.array(destination, _np_.uint8).flatten()
                if not destination.size == 6:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'destination: invalid array length: not {destination.size} == 6')
                self._destination = destination
            assert isinstance(self._destination, _np_.ndarray)
            assert self._destination.dtype == _np_.uint8  # type: ignore
            assert self._destination.ndim == 1
            assert len(self._destination) == 6

        if source is None:
            self.source = _np_.zeros(6, _np_.uint8)
        else:
            if isinstance(source, (bytes, bytearray)) and len(source) == 6:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._source = _np_.frombuffer(source, _np_.uint8)  # type: ignore
            elif isinstance(source, _np_.ndarray) and source.dtype == _np_.uint8 and source.ndim == 1 and source.size == 6:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._source = source
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                source = _np_.array(source, _np_.uint8).flatten()
                if not source.size == 6:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'source: invalid array length: not {source.size} == 6')
                self._source = source
            assert isinstance(self._source, _np_.ndarray)
            assert self._source.dtype == _np_.uint8  # type: ignore
            assert self._source.ndim == 1
            assert len(self._source) == 6

        if ethertype is None:
            self.ethertype = uavcan.metatransport.ethernet.EtherType_0_1()
        elif isinstance(ethertype, uavcan.metatransport.ethernet.EtherType_0_1):
            self.ethertype = ethertype
        else:
            raise ValueError(f'ethertype: expected uavcan.metatransport.ethernet.EtherType_0_1 '
                             f'got {type(ethertype).__name__}')

        if payload is None:
            self.payload = _np_.array([], _np_.uint8)
        else:
            payload = payload.encode() if isinstance(payload, str) else payload  # Implicit string encoding
            if isinstance(payload, (bytes, bytearray)) and len(payload) <= 9216:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._payload = _np_.frombuffer(payload, _np_.uint8)  # type: ignore
            elif isinstance(payload, _np_.ndarray) and payload.dtype == _np_.uint8 and payload.ndim == 1 and payload.size <= 9216:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._payload = payload
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                payload = _np_.array(payload, _np_.uint8).flatten()
                if not payload.size <= 9216:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'payload: invalid array length: not {payload.size} <= 9216')
                self._payload = payload
            assert isinstance(self._payload, _np_.ndarray)
            assert self._payload.dtype == _np_.uint8  # type: ignore
            assert self._payload.ndim == 1
            assert len(self._payload) <= 9216

    @property
    def destination(self) -> _NDArray_[_np_.uint8]:
        """
        saturated uint8[6] destination
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._destination

    @destination.setter
    def destination(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray ) -> None:
        if isinstance(x, (bytes, bytearray)) and len(x) == 6:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._destination = _np_.frombuffer(x, _np_.uint8)  # type: ignore
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size == 6:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._destination = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size == 6:  # Length cannot be checked before casting and flattening
                raise ValueError(f'destination: invalid array length: not {x.size} == 6')
            self._destination = x
        assert isinstance(self._destination, _np_.ndarray)
        assert self._destination.dtype == _np_.uint8  # type: ignore
        assert self._destination.ndim == 1
        assert len(self._destination) == 6

    @property
    def source(self) -> _NDArray_[_np_.uint8]:
        """
        saturated uint8[6] source
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._source

    @source.setter
    def source(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray ) -> None:
        if isinstance(x, (bytes, bytearray)) and len(x) == 6:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._source = _np_.frombuffer(x, _np_.uint8)  # type: ignore
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size == 6:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._source = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size == 6:  # Length cannot be checked before casting and flattening
                raise ValueError(f'source: invalid array length: not {x.size} == 6')
            self._source = x
        assert isinstance(self._source, _np_.ndarray)
        assert self._source.dtype == _np_.uint8  # type: ignore
        assert self._source.ndim == 1
        assert len(self._source) == 6

    @property
    def ethertype(self) -> uavcan.metatransport.ethernet.EtherType_0_1:
        """
        uavcan.metatransport.ethernet.EtherType.0.1 ethertype
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._ethertype

    @ethertype.setter
    def ethertype(self, x: uavcan.metatransport.ethernet.EtherType_0_1) -> None:
        if isinstance(x, uavcan.metatransport.ethernet.EtherType_0_1):
            self._ethertype = x
        else:
            raise ValueError(f'ethertype: expected uavcan.metatransport.ethernet.EtherType_0_1 got {type(x).__name__}')

    @property
    def payload(self) -> _NDArray_[_np_.uint8]:
        """
        saturated uint8[<=9216] payload
        DSDL does not support strings natively yet. To interpret this array as a string,
        use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
        .payload.tobytes().decode()
        When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._payload

    @payload.setter
    def payload(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str) -> None:
        x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
        if isinstance(x, (bytes, bytearray)) and len(x) <= 9216:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._payload = _np_.frombuffer(x, _np_.uint8)  # type: ignore
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 9216:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._payload = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size <= 9216:  # Length cannot be checked before casting and flattening
                raise ValueError(f'payload: invalid array length: not {x.size} <= 9216')
            self._payload = x
        assert isinstance(self._payload, _np_.ndarray)
        assert self._payload.dtype == _np_.uint8  # type: ignore
        assert self._payload.ndim == 1
        assert len(self._payload) <= 9216

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        assert len(self.destination) == 6, 'self.destination: saturated uint8[6]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.destination)
        assert len(self.source) == 6, 'self.source: saturated uint8[6]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.source)
        _ser_.pad_to_alignment(8)
        self.ethertype._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.payload) <= 9216, 'self.payload: saturated uint8[<=9216]'
        _ser_.add_aligned_u16(len(self.payload))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.payload)
        _ser_.pad_to_alignment(8)
        assert 128 <= (_ser_.current_bit_length - _base_offset_) <= 73856, \
            'Bad serialization of uavcan.metatransport.ethernet.Frame.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Frame_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "destination"
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, 6)
        assert len(_f0_) == 6, 'saturated uint8[6]'
        # Temporary _f1_ holds the value of "source"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, 6)
        assert len(_f1_) == 6, 'saturated uint8[6]'
        # Temporary _f2_ holds the value of "ethertype"
        _des_.pad_to_alignment(8)
        _f2_ = uavcan.metatransport.ethernet.EtherType_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f3_ holds the value of "payload"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u16()
        assert _len0_ >= 0
        if _len0_ > 9216:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 9216')
        _f3_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
        assert len(_f3_) <= 9216, 'saturated uint8[<=9216]'
        self = Frame_0_1(
            destination=_f0_,
            source=_f1_,
            ethertype=_f2_,
            payload=_f3_)
        _des_.pad_to_alignment(8)
        assert 128 <= (_des_.consumed_bit_length - _base_offset_) <= 73856, \
            'Bad deserialization of uavcan.metatransport.ethernet.Frame.0.1'
        assert isinstance(self, Frame_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'destination=%s' % _np_.array2string(self.destination, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
            'source=%s' % _np_.array2string(self.source, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
            'ethertype=%s' % self.ethertype,
            'payload=%s' % repr(bytes(self.payload))[1:],
        ])
        return f'uavcan.metatransport.ethernet.Frame.0.1({_o_0_})'

    _EXTENT_BYTES_ = 9232

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8jJ1Sf0{^{MTW=dh6n5HNoTM#jQ(AFTM^M@n!PaRKRFEo~wodB0F(C<+5TNPUJNB7oy}O#74KWDOA{7y7q!u#VFAqE*@qjA9'
        'KR`m_Pw-zjv%8MtBo5+*NRh`gXU?3<_kG8A`@gs|noIulsj%fnuIJE*OTj$xKC61%p|zkH29Z$Q=)=oO#x)g7zS0W0*)-?wnGel`'
        '9-uyJ;`wtiTdOhOX>!GsWPTI|QaM}!mp)g{oJ_3pbdAeM1ipcs9=esSH%&QL?)${tGkTOVrKG6Fibv*M^xq@0Ei0o3<^=cLPDCTr'
        'Wr|T{!_-gpxGp7Y8GU?CtaJA!_Ztdk?N)bghbi}Xllv-j)+3fsil$Iv4K2ps^dr&mxm)rTZ*bY|Z<JPrqF(ZxDd#cL8jBQd1}-=7'
        'q&~6Oc4V(PSMhAY9@+BTH%k~UjTG};Cf)6hK8>q-7(IooCREFm2X#NKdXdp*+TnJLF><x@yU~ZP2$dFL8NX)X>Vq^0jV8UEM6G5u'
        '@I(!hUf|6Di=nWWuZLVR706D~gR}+$`vZ<Xw!}lO#NKuX=qknzQ)u^CCH6cfTRV-=*BbL;ZXTG4a{ggd#mxI@Q~0J_unV?s7elt7'
        'vB#{}a-TKLJuK(b&lqdY*F%J-#a$(?S|2c=M_nE%;U_5=bmaz^SI*$sSQ;LT!-;J51U#LsPL=aO;50msEr2r^{8@M*If9p<kl9SZ'
        'Ot!k1WcO-naH*35yjCv2W&EGrD_|&gq8yBZSk@3L^KiW@v;)~{K%d>8hDEzbKnX)I+-4mdLZ)qV*U4|Jliz?INQ<AnenjW52EGO4'
        '7G(CjTUw;IrjxsHNk7vD74|~%$Tp*kM){?r6U=LS#yi7x$!c~Nk)5B*)_AV_FBGOP8cUF*On3e*l!LQNi&-EbGw<-8bu%;lAKWAv'
        'y}XB`fvM@43o~1uxE|l8X|&o(1=D&2a3O$I_y|6L4Y(hpK)4(WQe%p{W<wvLb*oR*_K*tKRP<4rLI4juPD6(D*F*Nh6IG*!7g4O&'
        '7wzsQGOF)976$^Wy9YvH^vKm#2+X^NY_-A|SCPF`@&<AR-|MI*7I-j)5z2lSkg)P?C>ech3rtSInRIMJjj}Q|PJu-joV3b`Qn@A&'
        'vl}q4e_hVxi)>vbwG2ZMVG(h8U7&c9YKxSL#Ufea4H4n%w$)@dRuD*(ID$?{X|^)!jI4l&h=(==KLg*xGZHnK=aC3m!xahY+g?z>'
        '6v42PE#Y#BPpN=ZIgu#zYiL92fh1{}9J4o_QJxl=>k7ZIOT%{1dkpD~6E94yQScM4k0IB`EZ5r<kG4~MIH_+kZg#Q!xITG{;o!lc'
        '(`#h)6sLvUX??7%-*r1M)0wsd-OrZ$EN;_FJ<@+1X>Sqg?<x3p6j{B;=G*zbs~}yjPA)OO!S|aAgLE~~b&S84c;?{pjU4IA?W3PO'
        '$|`?jY=6V73rMM!7cd-J^LlbQ4lVX0i<&irbRtaTPK@J^)a}ojh)l$x1=1^|EUuh$aBOgRU~`;<qwqGA;5T>&{)XRU_-q3{ufQgJ'
        'IRRh6*YFK|3*W)_@B{p)k0d{lx~T*|S=xM@aN%O%f-{v82kDo-OgMHTj4XkzgpQPaqPT2E7WSwJAs(Jrwa|^5;fsiV3w()s8wS2b'
        'B%1iE#KOR`=Vqx=UU_S=NQ*1ii%XT_%K2+IS7@;^Sy;HziwnPOtvY*ure=TH=Ko)olklkA*F8y-cETHJ=WpZg?auC_jEXz9e@=}<'
        '+zq!Ir=E9g|B)KsMNHkzFxBmR*NMfJ^AFJw<Scay000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
