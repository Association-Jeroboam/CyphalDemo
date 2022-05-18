# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/internet/udp/8174.OutgoingPacket.0.1.dsdl
#
# Generated at:  2022-05-18 08:59:58.974129 UTC
# Is deprecated: yes
# Fixed port ID: 8174
# Full name:     uavcan.internet.udp.OutgoingPacket
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import warnings as _warnings_


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class OutgoingPacket_0_1:
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
    NAT_ENTRY_MIN_TTL: int = 86400

    def __init__(self,
                 session_id:          None | int | _np_.uint16 = None,
                 destination_port:    None | int | _np_.uint16 = None,
                 destination_address: None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str = None,
                 use_masquerading:    None | bool = None,
                 use_dtls:            None | bool = None,
                 payload:             None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str = None) -> None:
        """
        uavcan.internet.udp.OutgoingPacket.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param session_id:          saturated uint16 session_id
        :param destination_port:    saturated uint16 destination_port
        :param destination_address: saturated uint8[<=45] destination_address
        :param use_masquerading:    saturated bool use_masquerading
        :param use_dtls:            saturated bool use_dtls
        :param payload:             saturated uint8[<=260] payload
        """
        _warnings_.warn('Data type uavcan.internet.udp.OutgoingPacket.0.1 is deprecated', DeprecationWarning)

        self._session_id:          int
        self._destination_port:    int
        self._destination_address: _NDArray_[_np_.uint8]
        self._use_masquerading:    bool
        self._use_dtls:            bool
        self._payload:             _NDArray_[_np_.uint8]

        self.session_id = session_id if session_id is not None else 0  # type: ignore

        self.destination_port = destination_port if destination_port is not None else 0  # type: ignore

        if destination_address is None:
            self.destination_address = _np_.array([], _np_.uint8)
        else:
            destination_address = destination_address.encode() if isinstance(destination_address, str) else destination_address  # Implicit string encoding
            if isinstance(destination_address, (bytes, bytearray)) and len(destination_address) <= 45:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._destination_address = _np_.frombuffer(destination_address, _np_.uint8)  # type: ignore
            elif isinstance(destination_address, _np_.ndarray) and destination_address.dtype == _np_.uint8 and destination_address.ndim == 1 and destination_address.size <= 45:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._destination_address = destination_address
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                destination_address = _np_.array(destination_address, _np_.uint8).flatten()
                if not destination_address.size <= 45:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'destination_address: invalid array length: not {destination_address.size} <= 45')
                self._destination_address = destination_address
            assert isinstance(self._destination_address, _np_.ndarray)
            assert self._destination_address.dtype == _np_.uint8  # type: ignore
            assert self._destination_address.ndim == 1
            assert len(self._destination_address) <= 45

        self.use_masquerading = use_masquerading if use_masquerading is not None else False

        self.use_dtls = use_dtls if use_dtls is not None else False

        if payload is None:
            self.payload = _np_.array([], _np_.uint8)
        else:
            payload = payload.encode() if isinstance(payload, str) else payload  # Implicit string encoding
            if isinstance(payload, (bytes, bytearray)) and len(payload) <= 260:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._payload = _np_.frombuffer(payload, _np_.uint8)  # type: ignore
            elif isinstance(payload, _np_.ndarray) and payload.dtype == _np_.uint8 and payload.ndim == 1 and payload.size <= 260:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._payload = payload
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                payload = _np_.array(payload, _np_.uint8).flatten()
                if not payload.size <= 260:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'payload: invalid array length: not {payload.size} <= 260')
                self._payload = payload
            assert isinstance(self._payload, _np_.ndarray)
            assert self._payload.dtype == _np_.uint8  # type: ignore
            assert self._payload.ndim == 1
            assert len(self._payload) <= 260

    @property
    def session_id(self) -> int:
        """
        saturated uint16 session_id
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._session_id

    @session_id.setter
    def session_id(self, x: int | _np_.uint16) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 65535:
            self._session_id = x
        else:
            raise ValueError(f'session_id: value {x} is not in [0, 65535]')

    @property
    def destination_port(self) -> int:
        """
        saturated uint16 destination_port
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._destination_port

    @destination_port.setter
    def destination_port(self, x: int | _np_.uint16) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 65535:
            self._destination_port = x
        else:
            raise ValueError(f'destination_port: value {x} is not in [0, 65535]')

    @property
    def destination_address(self) -> _NDArray_[_np_.uint8]:
        """
        saturated uint8[<=45] destination_address
        DSDL does not support strings natively yet. To interpret this array as a string,
        use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
        .destination_address.tobytes().decode()
        When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._destination_address

    @destination_address.setter
    def destination_address(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str) -> None:
        x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
        if isinstance(x, (bytes, bytearray)) and len(x) <= 45:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._destination_address = _np_.frombuffer(x, _np_.uint8)  # type: ignore
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 45:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._destination_address = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size <= 45:  # Length cannot be checked before casting and flattening
                raise ValueError(f'destination_address: invalid array length: not {x.size} <= 45')
            self._destination_address = x
        assert isinstance(self._destination_address, _np_.ndarray)
        assert self._destination_address.dtype == _np_.uint8  # type: ignore
        assert self._destination_address.ndim == 1
        assert len(self._destination_address) <= 45

    @property
    def use_masquerading(self) -> bool:
        """
        saturated bool use_masquerading
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._use_masquerading

    @use_masquerading.setter
    def use_masquerading(self, x: bool) -> None:
        self._use_masquerading = bool(x)  # Cast to bool implements saturation

    @property
    def use_dtls(self) -> bool:
        """
        saturated bool use_dtls
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._use_dtls

    @use_dtls.setter
    def use_dtls(self, x: bool) -> None:
        self._use_dtls = bool(x)  # Cast to bool implements saturation

    @property
    def payload(self) -> _NDArray_[_np_.uint8]:
        """
        saturated uint8[<=260] payload
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
        if isinstance(x, (bytes, bytearray)) and len(x) <= 260:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._payload = _np_.frombuffer(x, _np_.uint8)  # type: ignore
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 260:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._payload = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size <= 260:  # Length cannot be checked before casting and flattening
                raise ValueError(f'payload: invalid array length: not {x.size} <= 260')
            self._payload = x
        assert isinstance(self._payload, _np_.ndarray)
        assert self._payload.dtype == _np_.uint8  # type: ignore
        assert self._payload.ndim == 1
        assert len(self._payload) <= 260

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_u16(max(min(self.session_id, 65535), 0))
        _ser_.add_aligned_u16(max(min(self.destination_port, 65535), 0))
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.destination_address) <= 45, 'self.destination_address: saturated uint8[<=45]'
        _ser_.add_aligned_u8(len(self.destination_address))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.destination_address)
        _ser_.add_unaligned_bit(self.use_masquerading)
        _ser_.add_unaligned_bit(self.use_dtls)
        _ser_.skip_bits(6)
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.payload) <= 260, 'self.payload: saturated uint8[<=260]'
        _ser_.add_aligned_u16(len(self.payload))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.payload)
        _ser_.pad_to_alignment(8)
        assert 64 <= (_ser_.current_bit_length - _base_offset_) <= 2504, \
            'Bad serialization of uavcan.internet.udp.OutgoingPacket.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> OutgoingPacket_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "session_id"
        _f0_ = _des_.fetch_aligned_u16()
        # Temporary _f1_ holds the value of "destination_port"
        _f1_ = _des_.fetch_aligned_u16()
        # Temporary _f2_ holds the value of "destination_address"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 45:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 45')
        _f2_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
        assert len(_f2_) <= 45, 'saturated uint8[<=45]'
        # Temporary _f3_ holds the value of "use_masquerading"
        _f3_ = _des_.fetch_unaligned_bit()
        # Temporary _f4_ holds the value of "use_dtls"
        _f4_ = _des_.fetch_unaligned_bit()
        # Temporary _f5_ holds the value of ""
        _des_.skip_bits(6)
        # Temporary _f6_ holds the value of "payload"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len1_ = _des_.fetch_aligned_u16()
        assert _len1_ >= 0
        if _len1_ > 260:
            raise _des_.FormatError(f'Variable array length prefix {_len1_} > 260')
        _f6_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len1_)
        assert len(_f6_) <= 260, 'saturated uint8[<=260]'
        self = OutgoingPacket_0_1(
            session_id=_f0_,
            destination_port=_f1_,
            destination_address=_f2_,
            use_masquerading=_f3_,
            use_dtls=_f4_,
            payload=_f6_)
        _des_.pad_to_alignment(8)
        assert 64 <= (_des_.consumed_bit_length - _base_offset_) <= 2504, \
            'Bad deserialization of uavcan.internet.udp.OutgoingPacket.0.1'
        assert isinstance(self, OutgoingPacket_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'session_id=%s' % self.session_id,
            'destination_port=%s' % self.destination_port,
            'destination_address=%s' % repr(bytes(self.destination_address))[1:],
            'use_masquerading=%s' % self.use_masquerading,
            'use_dtls=%s' % self.use_dtls,
            'payload=%s' % repr(bytes(self.payload))[1:],
        ])
        return f'uavcan.internet.udp.OutgoingPacket.0.1({_o_0_})'

    _FIXED_PORT_ID_ = 8174
    _EXTENT_BYTES_ = 600

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8j<tkh0{`tjTZ|mXaXb6gQje2pNvDUUF)dR|`?y+Cq<Erjg(s2@nPyQ3iWHax&T@99_h!i1nejaCZUqFOKN8Tv0@=hHfS>$`'
        '0e<o)2m|E7ya47a{NyJ;85l4a7)A)>Cso}uvom{l6kn&<))Bb9y_xRn>UwomS9SAZ`LBMZ7sS8e+upzk47=3{xNm8;^|{uyd8?zl'
        'ea{W7kdKGY9pSds$FIiefyc)`9q;<__>afUVYOp94)@1qVffsqp&#jC<nw%!O2^Uq2x3R1E$f=ovYe3n4i8(A;k7=A!X?*omKHVr'
        '0uRT-dS{vYf#o^`vG!T~{ikDAV9KA4e>@&;>u6!<Tiqz+!T5&=egoXoR^wsi2Nt)D2||sIp@mu}BrG@T?)fxZYZ+T?KjQ?}lEaPT'
        'i1-rs^RwI5=~`jO=FU=Rj@b+X*R>$*^j(9G&DVynEGB@cTk9~s1A0X>`jhdg@$hS%Ak-W~^NlQ^OHtQs3>yItX#O3`7!S)G!_~)U'
        'Pbh`LY10bS9!*NcF98qL&{Z`@)qDiuYyLo8*6fI@-GLgKT*XIDfJlT$XVt;cRm)Lb-{3y=>vEN*Okew2sGFjT&jZhO0^V4$LixmY'
        'b<MU1>ILqFs_r5wR>PKh8sGFHM-LH8)$L)+EN07=A4Z~=WpF375CRPonp#MW&m38N@A#tXxqjGiqJ9^dO%SQ0Kp%yLu#4ySIrm*P'
        '(0ZJ}^#o1<cZ_sShRXx|7OJMU%+-Emhn9!aict*^M8mKGqCsQ@CISvuIColOr1Z;@m*%YbM*Qt9He<eRe$#wMGGfNy)KjBrb_n0G'
        'xpVj?;;&|2h>56jB6+aGH#U$_-`57?;j5o%_!OU<5X@hor+FcJuETBKM-ob*&7fIN(HuU5lILl<6%NL1_wc1ylsbYN>-PHwQ%D45'
        '?{cSW2jk(+1k;HyBGTdX-{ax4A6ucs_fz~c#&lTfxZZfEZUiJ4^t-NY>8Mn|`!3Rf2=|G{eJynTtX0uX3su%UI(+%C>*!j@opqbi'
        'q^YIP9Wn;k{)Ll~ZKDdTX<6+EsT%+JxXJ3HplkkaOpM>dUay|goF#sWdpxu@Lg_-MudO0!vBN3x&^(jC67=g^4k|T$!De78!x~wE'
        '$kwPoQ>blW#ES9nlK9OORvfW%{H&5bV<lD|v8w#LNZ)I@cdWvyBUX?5J+tN=t07*jk@m+Y`1iJT+p%X@W5k}7@9H$xa~rl}+t{-s'
        '_IwU5KE-D*Jg^UYjy*qOGw~QB_Tm?|W-qXr5qoLPNcaYyZ-1!%>_zs{h<#1AE#v!Vsqf1V-Ir}=UmLMk*2Mwe;=5NL2^M>qy)t66'
        '38fL2*B-e)dzH<O*y|hOge~y>8;=E-y~bW2u{U${!nX+T>yHhOy}{lbv9}(GFSf!qZ$Hr(?Cb2U5mQsz64u{%Vu<W*rjFPS2}gYp'
        '{xteGpUQab8*Imjy_1ZY;R8|WTTg8a_D%NAi0%AB&R`D}TVvaIpX%7`TWsfuHIsS9Jlplu$6)WW=7@d!q34M`u>E&71rN51eS5^_'
        'CcJ$IVK%e;-Mwk!vhT3D5o<jX9k3VndGG1tlw!nov(|{UCsNRqa<J#|#>|hHr$IU%dyln8Z0{pe0()Y=_cz8Yk5`@&c{=1dlVZj8'
        'u)QO;Z>@aHA<T9nBm46h<SCP<OP&*XKI9}L9shl{Z^S-$EZVTW)c3$z`sDeR=UQG)vQm<j5kVQkjqM+?`Mk8WNnSooFwXKMFDrRT'
        '$;wGqN-{Dc$73I`18jc84n8(b5CZo9?u0IDr6wygS&7NYOIBK9SrPalcI-oTaKyg1vE1xKnDZn%-%qf}N={a8vQm?knXJT2$%~{A'
        ';_zMey%GE9iRi=*5{%!OmZ7W!W#uO;Jzp$4f=&|4Lu+IRc@$yz&R0DQmuc5Qwzvod1sh$0x`ORSFr#48%P^~8-z%Uh*!?Or6@+jN'
        '+6oSF9p)8wh~0og3OmMb!ZC#{vRkmIu(RwooK@I4c8A@Ea|$!rU5pc$$L_J!QPkxalxP^4b-`0i{Wm6PsFSm}$w5P%F#gI14dfyf'
        'wt|LD2^s`#pL)=sevu*EgrGsq^WnEPXiz7C-d84QpgF%Ixci$CG;9(^nV>;RK{jZ3(lIwLXm}XRo-Am{%g5TFVRJ%;y-z7<c=C{8'
        '=NAMGiL|t(yojLT;X{Vk|DS?}^+Sf|pJLD;*Ng`T4b!so>lrjW?T}&rnxKJbCH;jsXfS_<k10yH$m$d&Tw>_8Vw^xR0)`4t5+_iU'
        'a6c0#U}PXd1xh)Xjp6oeUP?0zp9jI%+<ErT%7wxax35`_O1W3n_0{8xYTQ6wF}cr00?pF~wyPOxV7ifQP_nJ(`YW1ma6=8<R^y}_'
        'a+$8{`q+*#n+X&is2W1iY};MI)&z2ndaHa@>w7l-v3LLeR`#dyaRP&Kb|SIZ*Mc8K+}A`Fk2{nDGt?E=zYxg$9^t;C4OA^qBggu}'
        't_MXgO1<_QA}1KnE7UGfHqjSJPTkZThuefXWk!2FOUIe`)-nOYnGy)s;|^jX5_&z~?W>wIPy;vebuJT_T;?2!G!364B0-4lvpBUH'
        'GB=8&7#U8;Y#6p2h+HLK)j4+DyZ?RF)k7WzbE>B6t}kX4k96eZr)uDF-9k(Sr(2D~1JBfK)uQw~F+vSO-@^WW0$=3nb7@|m8<8%#'
        '-sgSSN1{4LN`P*J?Xa~Y8g!%Jpt^5Ak;>NyY|v`t{-oqCHPrfU<cM5u;Awg+D)^2_V);Ud@Vkfd!ksWqBRfk-EF^6ZSd?}~k?9iv'
        '%|Q`e{vZ*rMpHi6x4W--9zx2#+|^Q#N+}BtHdJ*7!if4UVwx@p({lZ#9qNYvc4s+4{r7yhx3%Yk`PQD+o(FWx^e4npOcB7|c6-mk'
        'w$YtGIKN+e|6m*c$&Yz$FF)9R|3LfTf%o6vw<8N6oz0w-5+XzjD+MJXOaqukCId_84C;&4b(c{IQ3FVZiO5alLy!B&mR&T?!pDb?'
        '9Nh3DCCPsL`LMkso^+NQ8NAhIR_^BVva>6nVt;M8?PJ%qx#r|@+~!+Mk-6-j$dr2&@J?2tDCNFzbQKjLRH=SL?P~f3wQ03@YYrtn'
        '5XC1G13;pOAjE@{3#ZWrptS9pO85U_{juvbwh`K7ONW1S2B93m0hfHOub!q_3Sk#cXam%&Pq`lXRyb&>M|{_djVhJ0P>sTo(<eS9'
        'bs$X-B9FRpqt*Dt6XgOuTU!bQLfePWE+PYQlKDy%b9VUp`jrFAE|rATKf_;HD&j<{0nMO*n4d2yg+gw+d*g5W*DWA0=b@~aA5PUk'
        'd|$r%$Xt*k9LeO(Psm4~Q06_G5}(PZ*Z&~?_CtcdUh>@3Si$UqTK^5&_1a36Z>7q&QsrBz@~u?)R;qk+Q|0e&TC)5RM%}cO`BTL2'
        'v6APTh|8v=(l-%T+O>LMa{Wuh<Ef|IzeKzrBN_jt<F|>a`Y&}3?ECDajgt9dUyc=^P=rDm3RNi7X@jl^^)lSAK)nj}I&IVyVWtc-'
        'RhX%>S(q)tY#C;&aK8q#b*6$^1houm6~hzOgk}+%WoTAe8`?!^m!Vx{^Dtk8`7+E`*&#SoghORGRAtBDSP_nu;aHU|!eS8?%dl8w'
        'XW?uS&X(b9m7RlgML1W6b5&-7Sp>5TW|ev16~QZmS7ocPT7=aytXA1YxLAaXWw=;nm*7$nE|uX@m5pFjgi#qrRdyLJ7vXXlE?3zV'
        'xKe~GWw=shSK(?Au9o3ym0g2tMYvXmYgKj~t{35Y8Ln5^4Y*N+8)djrWjEnw5pI^@W|iH7TSd54hFev38*Ufjb{TG0*&Vo3gga%p'
        'Q)PGIZV~R5;ck`PgL_4|SB864b|3B+;Xcw9DXl=E1ceF|YEW08UV=IjyhfX%GbNa*zzkAXf!PwwR$#UUssd^W)C#CIXe!VwL9+tQ'
        '8nhK?m!MsNb`9ngm@mP61?FpTNP$BoI8=c{H8`fgu@W4sz_A)EDzI3B#R@Fe;H&~?OK`RVXKQdyfpaA|SAlaiFcmOMU{=7afv131'
        '0<QvI4OSIcEx~F9R%>ukfr}-$Sb>W*xTL_P5?rdlr5cPB7?ogDfl&=ED{#34mn(3&23HigQi3ZLxKe|w3S2G0)e2m#!8HZ0mEc+h'
        'uGQeW0@q7$y#m*3a6^F`CAd+68#TD8z|9ietia70+*06H32s&3Rt;_|aJvNeOK`gaw`*`mfjcF*Q-M1*xU0b365Or8-5T6e;9d#t'
        'Rp4F??ki~-$qWY6?fO<3$yPwUCZL{?bl3{0HzA-#cU)3;tBho;jO5q8jHH?8?^imYo}_iR0_u$mOQghX1=NokP_I{bvK3H2dO-a!'
        'g(_PC_0tKcH!5_QgwryHPU7ie986OrO(FGcT}0DWimI_iZNp$1n)OUPjbY1Xh13{IV@yqfb$R`ennLL~s@@8ze_KOp8Bb$i{m>zG'
        'Ty9m1>!ql~>XcF_9PRbEPIo&bg;eqN1)@A*#j@?`imLc-g+7&4nQjoO%iQm3q1A6S=rRFWIS|M)8oIcEid6cpDAv*(b$@$a?G8d7'
        'P`yl2x<!>lIEvxBqA;UNbxM8gFz`gXhVJ(JqIOEu98g`3M;8gS)KgRpLO7lJ!D02lhkHal(B6F?v_%yc4re*L4eo^|BD`$zm9*-p'
        '7x_31U)FlaI-tI`YW1UjQu+{BpYunpIih;1q#B}r*mdYuj4)FPkts`1vsW{`cyi%%=jh4Pr+&W!$4_=npFTm{`3Sl5hXF?#8b54+'
        's0R@Ph?=!*b<zdSy?l*`iq!EfYHAZ_1u;U^=2ZJ8uD6&JJt5=xoEkYcRn;Moh6I3ZTx4udRK`(lin?N2x~b}#tVbE-D(3{9`q&{J'
        '!{<6;U=OHz#YmAsAU$mvaY2?kd<DtxI!G_|L37L8>_J6k{l1HW$tSbf({5+s=cv#cn`ee!Pl`|YD%Eh&p{U%=DD_i9sx&*TKRGje'
        'rblHz_%y)xKZw8M`(b7NgMIDxm~NaPb>hSAnVVcX-GRI%hB*8!^A&T>Y?}XNw#@%Fe{TMd`OEWHkfG;G^l_Cw{+dc#hTA#@6_?TV'
        '5XSh@@cB;9TIGhgpo6YVfnU5me6b_T_VAU>JDwJrV^ZVLw5{%V_{^dkSgVWl^rz$IP<d}WESoM}R#Wt>@i3P7Bgmfd@C`5O+Lqq&'
        '`BG%lh?84naH>^#xed-ax!z_xEJcPl9=<uh=fJ+Hdv03o)}9uTb{x_jFxxw(79esy-S81`f7#Oc_$MgFzj`&k?4^&?*Oo*PqhMFo'
        'TF3%LS&$ejlenyf%J>BDa~3CVaXiM7N<%gE#KOr|qp{!&BouM+%B0{k9X+|=h2~7{(ZET`69$XKk8U6#k;9gG!;{`4vu5C=NHah)'
        'tD`u`n`q>SK_fe)upY5F&6TglhShQmOUQzpDYX`rT2UZsL|0K3QLRvK1o@1(q^sefG9@z<<z!S$XGy_E;%ZA|FXb$(Akix-z~aWP'
        'milRgnk}i2Sp1~SP7pt6?C4K)bO(~{xG0h2qLPgo5$%M{4hBKU`!O7Oi%n|#3F`?Q9AC3+p{I?b8X}N+MK=Obtyv%uNa)4UA`Q}c'
        'S~w)<!CY*a#E6a-M!vYMNB23Bu_2H$_>#{BL*->AzOd?!p*gxV=RGa5>4F}c`}mB@JAtwimlWYriExi5G_gw!50@?O<B&K<10Tg@'
        'p##;3JUeD)A`4Q`4GR}tQk0|~H?2n&mNsFX0G`yCCcwxlVWZG@X<ags`;n4+h<rD6b=OAX1l;b4iIAQ4GbS@!aaFgwY`Ia;2yh__'
        '`I42$e|%jL?|Zg8m_W~v;$Wje1)B@HPM0XTjxAgCEFVF~)5KXUIYgzD0?DOFnuiz?vtt_{4;#;bN`SdW6{KoH@x+4=eC+d36Ml(<'
        '>kE#A!az&gv_patV{p{azU9b;JE1aiTGSGwDv2>rAh<+E=eQUcq)$<Q8dX`#-KC0O8Vz}Exu~Q<`Q}hgv5AKB5VsqJ{$Nhlri%fR'
        '3!YFr)2p4N(uiv8<c6xCC5gJ|yEHFR)}2TUNrY}kqL_MPa%w>k^|RE>(gSTqAkfi7nKjyG?$42^&|sos9LGy(5SM}n()Rf7vL(h&'
        'aV7E+)e;nZpROGu`y$4$P;{&;COZC!l1@HeJVsVACL~a$O_`|Jr1QHH{kW~wwQMUKNT(xk?dA9!K%yyHziTZ;qMmiZNhBR*z>YHZ'
        'Pm}VSims#&mC$F95+sO4Su9Cfm^dxCa(EeqBn9h{jS<E9E*dVB0&I<x&f1#3=4g^uYOHyKY4O5w`ea~xS;-YfQ3}omJQmiEL``Z+'
        'T3kFQ%%n*i#{P(~Me7I3q178SCWXea^VM}D=^&z9yXin^Ooc9@o8rX>5Ksw3&9qN54AKBWoNO?;Se_f{>L8Gjw2ckm6!y~IhFmut'
        '3x$vLavi|PxC@TELQXxpk0H@b2yZ~=LLgIRJxA+u6OG0ackq$DOFb!@s|)ez5m5nc%k{8{{^Bl)fgnrF(*_O~&r;gKKF2=dm;jfz'
        '(9v?{N;c`PFJ(p`DvF}f1obRBfYIgXBNIm-bYESvkOvbz6okqUNh;*TGfKP`WRJ9!jj2FwF3;Qbf(D)YGCoTTtCRpYcJwA_Ngtt+'
        'wxb0)bO{u#SCYd)a&_XA^PuiXJ@Or~ag0}Ta@<J)NVrhR`m}I25{sV+SZH1pX$ay{b-6e)v0Ly=5<~csldJ2b=&sO_o7jaAsv(ZW'
        'OwUaax+U~~5qnZ3x$nUIfw|bIOkm=iQMD0JvMOeMnJ9FTla{z&u$3Z5?{*(Ql8DKKaS}oFnAP-D$r{8Yn9syDf-wMjE8*lu#c3fE'
        'i%8;r2t(kCFjp>B7-+<o4aN>M*=nA8hA5+_rwzh-LL-*Ue5g6dhnQ=^SyhIy=x^X+me^7eC$7<Q8EgsOrRs;$m-=5x6i%j}Y-5nn'
        'W`Z{<0$(+?hz>Lf184>7gsLtAq-iAKBiDRfZTz{6ut^a>t2v-ivau}*782~3wk#LNSZTFPRFecX86BRRmK!Piy2<qmQxSY}?x~UU'
        'W~BDS?2Gp@M2I8|>corDHaZTc#tTb2P@-?-oJeCtKF5RL1sH{j;6C235iqsbkkQqdE-rThL?b&>OP;ey10Ml3-A>XiPq+!9tqgXg'
        '^CSXE^_Xz2k2@HUO#;w#k&GKz&axYaYP72nkV>tgxHRi@lW0yD)>`pcu91h0DbDm!BrROLkpxYQ{9^$l-!9RWU9oc{Ce587^7&-h'
        '&MKG;TCiuAHeP}YbaYTenUe)75V{q6QB$ERvP>LCBd5eB`5-OC=aJ)+mdfC2A&mrWbWU@Cl4vhkj7-Z}i(`gJnPoH48nFO5ZX?FS'
        ';qe9@*%s2$Ud&84_NvlIH&5-gJZ!0pq;T<SLa~sL8Zvm+<f>MRJL9fWpeV)`#z+R9QyYMZu~^6O#QrcUb#_0B0wT>0CLT|+^M^i_'
        'CwvX7CnimnChH{_+|~xd*7{OW=sOyR#$>4%*vF?Q38^1NZm5wJ#^oyN_ch=8978EFCvokpm>{+{$>COAU5}80WKUz=j5qaS`cAA^'
        'yqA?kZt*e{TMwZW=|)K~wNpaW%y0Wlc0rPz3lx7Mfb`KP(RylXrkvL`v6@(#DIA(|T6wxLn>i&*zEvD89hJKQ6V;xa{7h_D3?QD6'
        '2xuf5g9ngEo=BvnFnj1#oCp=shLPPa&0U_G98Q)|lXQ+U2sD!Oj$%1N4K)Vx$mrzc<MckO@Uw8u%~;<HmN2>-V~Qlr9F(TRj<NTQ'
        'k0v|#QV8f=u8x+1<jf9nkR?-$nxcvhzuf9^LNsi2ZE?<LNF5LnDdmme6pCxuC><(X`Qjx+no(ps$-INQDlPCd;*;&&6iMtX!f@Fk'
        'AuV6E5(hwRRayRIZ6GgKaunAQ>hHK&5OLRZ0Gge|iJX443DRW8h;_NH(J@WhUy{y=NGnL|Ef=75w#8H6a=#9}5tO7|F#>LH+8rQd'
        'JzLY$6@oNNA~Z$lR4;?Id7IReFfuX{>(fG<8}Lxskp~9yP!Fd9FuG0MMi{9_MtZx(0Za8yreNfv-H_r$He^n&8q)dEa3$`0VK%DN'
        ')^`l2&XkMO!4qB6>?PMn%JkFiNkqcMwc3g2pPZy6Kaea>dJ5L_E$WGE!%=M+z;?6e{L|gL>`v}nBYQMmY^JJW-&}0%>0GjjrlQ%q'
        'N#@d}V`8UT>Y2pUn${9|>Umt~ka`1+jdg)kPX>;j$VZ61@mTJXt%+neGc<itWDjLLBZ%v48oJKzu1o$HX{EbSnoW2V6BL$_DE45o'
        'Zn*)^$2W%;PKvpW*FSK3bofGiP<YJ+)%bS(gSqL`^Z%(73SXVZ(+84=^^PZLH)cu{mq_D}j*WhH5+6)=kag55Hd50@=eHFLg}8hE'
        'jd@JAZ<<{gDeHEadX*bcNeA48t^Q(t08_6v0Pt;W^_S}dn0l21P)z}}vDM}E0ZhMo4k<1>9l|#^pPA}ZkJfo5lj-I*^I3Doe33Z#'
        'irF+<=FiPvn*S?ve3ahf=l=#jA0;1n{%`T~()sK73BP#z{NK@wzsHZ}`G26V|41MIL?1Wk<Dco{U+Cjs>Eqw%<KOXvGIHl{;+LP8'
        'JJ0_I{vOskd=)K3IEEW94PWUP@&AP3cT8L>@z?a-`s!mIn^!kFHh;GGpkwnlULw*a1^I!XaVooTXPvjyx%GeU>DfR4WB>p'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)
