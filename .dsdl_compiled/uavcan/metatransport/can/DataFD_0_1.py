# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/metatransport/can/DataFD.0.1.dsdl
#
# Generated at:  2022-05-06 20:25:54.689044 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.metatransport.can.DataFD
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.metatransport.can


def _restore_constant(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class DataFD_0_1:
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
                 arbitration_id: None | uavcan.metatransport.can.ArbitrationID_0_1 = None,
                 data:           None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str = None) -> None:
        """
        uavcan.metatransport.can.DataFD.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param arbitration_id: uavcan.metatransport.can.ArbitrationID.0.1 arbitration_id
        :param data:           saturated uint8[<=64] data
        """
        self._arbitration_id: uavcan.metatransport.can.ArbitrationID_0_1
        self._data:           _NDArray_[_np_.uint8]

        if arbitration_id is None:
            self.arbitration_id = uavcan.metatransport.can.ArbitrationID_0_1()
        elif isinstance(arbitration_id, uavcan.metatransport.can.ArbitrationID_0_1):
            self.arbitration_id = arbitration_id
        else:
            raise ValueError(f'arbitration_id: expected uavcan.metatransport.can.ArbitrationID_0_1 '
                             f'got {type(arbitration_id).__name__}')

        if data is None:
            self.data = _np_.array([], _np_.uint8)
        else:
            data = data.encode() if isinstance(data, str) else data  # Implicit string encoding
            if isinstance(data, (bytes, bytearray)) and len(data) <= 64:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._data = _np_.frombuffer(data, _np_.uint8)  # type: ignore
            elif isinstance(data, _np_.ndarray) and data.dtype == _np_.uint8 and data.ndim == 1 and data.size <= 64:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._data = data
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                data = _np_.array(data, _np_.uint8).flatten()
                if not data.size <= 64:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'data: invalid array length: not {data.size} <= 64')
                self._data = data
            assert isinstance(self._data, _np_.ndarray)
            assert self._data.dtype == _np_.uint8  # type: ignore
            assert self._data.ndim == 1
            assert len(self._data) <= 64

    @property
    def arbitration_id(self) -> uavcan.metatransport.can.ArbitrationID_0_1:
        """
        uavcan.metatransport.can.ArbitrationID.0.1 arbitration_id
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._arbitration_id

    @arbitration_id.setter
    def arbitration_id(self, x: uavcan.metatransport.can.ArbitrationID_0_1) -> None:
        if isinstance(x, uavcan.metatransport.can.ArbitrationID_0_1):
            self._arbitration_id = x
        else:
            raise ValueError(f'arbitration_id: expected uavcan.metatransport.can.ArbitrationID_0_1 got {type(x).__name__}')

    @property
    def data(self) -> _NDArray_[_np_.uint8]:
        """
        saturated uint8[<=64] data
        DSDL does not support strings natively yet. To interpret this array as a string,
        use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
        .data.tobytes().decode()
        When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._data

    @data.setter
    def data(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str) -> None:
        x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
        if isinstance(x, (bytes, bytearray)) and len(x) <= 64:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._data = _np_.frombuffer(x, _np_.uint8)  # type: ignore
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 64:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._data = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size <= 64:  # Length cannot be checked before casting and flattening
                raise ValueError(f'data: invalid array length: not {x.size} <= 64')
            self._data = x
        assert isinstance(self._data, _np_.ndarray)
        assert self._data.dtype == _np_.uint8  # type: ignore
        assert self._data.ndim == 1
        assert len(self._data) <= 64

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.arbitration_id._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.data) <= 64, 'self.data: saturated uint8[<=64]'
        _ser_.add_aligned_u8(len(self.data))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.data)
        _ser_.pad_to_alignment(8)
        assert 48 <= (_ser_.current_bit_length - _base_offset_) <= 560, \
            'Bad serialization of uavcan.metatransport.can.DataFD.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> DataFD_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "arbitration_id"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.metatransport.can.ArbitrationID_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "data"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 64:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 64')
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
        assert len(_f1_) <= 64, 'saturated uint8[<=64]'
        self = DataFD_0_1(
            arbitration_id=_f0_,
            data=_f1_)
        _des_.pad_to_alignment(8)
        assert 48 <= (_des_.consumed_bit_length - _base_offset_) <= 560, \
            'Bad deserialization of uavcan.metatransport.can.DataFD.0.1'
        assert isinstance(self, DataFD_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'arbitration_id=%s' % self.arbitration_id,
            'data=%s' % repr(bytes(self.data))[1:],
        ])
        return f'uavcan.metatransport.can.DataFD.0.1({_o_0_})'

    _EXTENT_BYTES_ = 70

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{`usOKcm*8OL`iQlj3r<%eQ>;)&zO_(e;$lGu6LvEw?OP!*iS4H~5DrMT9tLXiZyRHXm`oI?v6SRewt1=5~^9*Ur+'
        'peG-5%rQsbnxoNEjz0Dq?tdtfdRSH^2W=R@`44w@9y>d~|9;=@>Q3^{|9H!){}&!AFXpTHLdL0j72hrRpSih$mvN>`bLCRi54<QG'
        'd_Snvrh{6=`(Ux`Mfal<UqqirB1}0&caHWSs=4#iZZR|G1#VDri`8<e5@ht2t8U<4yBdXQXWpw+{ZcVfR@ieB<@=Ger2VJpizw`O'
        '+#sm<xmw^=qfe;qHAdAqDhgBAe6NsS9!;N<r{0`E50QH5{jf-Vv<z6K!eeU=^>QWW)0TiLy?ZrMJ*w9XP7Tn2)DE;Uq7sePPOjP7'
        '+ium{aEoi5Y`Nmk`GG%ACp+?CvFgthz5Khyz?<<Ztrw!-p`M(ASDXn{B>QP9rrm1b%$4#q701H8Q>GzZEpvtTW%VwafBTQojVRph'
        'R0Fq|cPshkhVIpJbdITcw@{-IB%OR|Its0bwhn~@Q*J)*7iU_p0iDYJ)lX%<<mYJ_+$3opx;iEIRH+v=q0Xy`TFwhcnihhSTZ~s2'
        '9e7S1snU7oy>i8yb^|XT-3y1D+x~)=cl4|~)c$0+)2Wtfm1&Q56g;Qw(piK(S_*zH3VWw$K`%_{t@mlx?6Y)Ms-#zNcR=b^qp)kn'
        '52CQ|%3@i$g{$6NDGCpiYq^3y?Nq#(T0!@`yw0dXcf14$l9ok4E!DT~U$GD}W0~=co}wtwQ$OM;w@M?ec*Q`^*}OmPMfcSCaM$?w'
        '8LGzpJnivs`(7oZFG8+BogOojynMB&ZqWWa3J2cygZJvc->09L^svh*m7|ca)kt-5E?1&6rom-t2Ivy%k^iRb(J7QF%d4*2nN~hs'
        'ef4oTjODQ6AazT9(kOi#?zvJb>Z?~=waKtIZjt6fdq7joTvHpvleI#@tt_sn-R;Cn^~*@e{-tV;T&Elli`IE9N0T?_7d0MKa2Ir;'
        'M<YTPRktl|UC&yQ39a^$?9!T8l1Z&yOEQJ+-C9#ivPWxjNv5&C7svPExPG)Z5RXR=LWiKk&>hg7&|T0G=x*p9=w9eP=qU6#=ziz{'
        '=s_rhJ`X(v<<J+PhoLV*k3f$?k3o+^1@r{;B=i*YH1rHK13e2JgN{SbLC-@cpf5pRhQ0#50KEu(75W<Vb?6(=H=%DqFF~(EKY}Xg'
        '0`xBQE9f`S2hi`K5225sk7LcIZ4^dLL72h?Q@CylADMzOg#}Z%YYJbP!Z)Vyz!bhWg@>l_$P^x<P@}tqw@@a((zjx4%c)B2%Qd}W'
        '4?*OSJugVE7U|z-D=@LzFtLD10+=M)FtLD13Ya8-Ngpst1CwrGk_09RU}6E2VPG-@Oa_6;KpQ4~z@!(Lq=88fFzE&+DPWQWCSAZJ'
        '0ZeRQVgVBlOgJ#%z=Q)64oo;O;lP9g6Anx`FyX+20}~ERI56SBgaZ=}OgJ#%z=Q)64oo;O;lP9g6Anx`FyX+20}~ERI56SBgaZ=}'
        'OgJ#%z=Q)64oo;O;lP9g6Anx`FyX+28%(&tgd0q_!Gs%3xWR-QOt`^>8%(&tgd0q_!Gs%3xWR-QOt`^>FVz$VN^JZ=rfVG<Iy7`>'
        'AR4N<dU}w|QGgr8(fg`7QfAE@>74}%1oK{g<C&L0>6B#Zv>H?6Eh!2H@p9wv*G!Jl)skbVH$RVN|885>?BD2rRdwl}x;&}gR__RP'
        'P5nw;SMRD{E2-X7Sv46xzv?JkgLrkL9<ZOgxFTRzAE@8PgZSO5(d_az6(9ELT5)gleVNgHnas$pn-L>3Vyl=@djxC4jFN2;tPL|t'
        'wMDSKFryxrQ3__%1v9c?Mnf>8L734%TLjw&GwOvIrC~-rFr#jmQ3__1gc)_gj1n*-8)js|j2O&_!HgKph{22)%!t8^7|e*lj2O&_'
        '!HgKph{22)%!t8^7|e*lj2O&_!HgKph{22)%!t8^7|e*lj2O&_!HgKph{22)%!t8^7|e*lj2O&_!HgKph{22)%!t8^7|e*lj2O&_'
        '!HgKph{22)%!t8^m@y+}%!nB?V#bV^F(YQoh#50t#*COTBWBEq88c$WjF>SaX3U5gGh)V!m@y;P9=3LM!q(1>x^tuMgsmMKIy9^i'
        'wx&IVbx~7LC}#gc0iilL`>zBAhkvDVZT;YI?-PT<gI6w3^4k@6&g1U#vHZ4vY@Uh2VJC2Bocb@kxL6Kx({YG<m&UuPD6;vMnAQ<v'
        '^MlyI`rDEAN2qbd-_QP&PQ7yn?RZAVGwPlZqaX+cu?`A$8wwUsNCJga8wyFFV6`P$NuXc@g#n<@2Ncpkp&KY9fkFZ(SU_O}DC`0X'
        'JAuLupfC&+hJeB#P#9=?RnP|%dVxY3DD(h@ZlI6?3Q3^Q1r!oM!3GKzP!K>t00jXQ1W*t_K>!5-6a-KZKtTWn0TcvK5I{iy1pyQU'
        'P!K>t00jXQ1W*t_K>!5-6a-KZKtTWn0TcvK5I{iy1pyQUP!K>t00jXQgh4?V6of%R7!-s-K^PQ-K|vT4gh4?V6of%R7!-s-K^PQ-'
        'K|vT4gh4?x2a_EdIyC&^X+SVJ)D+t3?-1IbhK2{$_?V?qaTlX--%Xdc(w6v5{bjwi_4|%N$18Yq`U`>8g2arp^j949P*J}^cgyay'
        'A1p@lQn<^!*xy`;x#4hf-wn4o<K6JeUf{3wvB0PCTlY(C4>NUJbw{z(V%AEmV=0!jSHzq3ZL+KJRMVng#$p=#WJ+V%VmB@OWRJ$U'
        'uTh`2q|N*L_Tyx4BWAVem$9c+kCXk{K89M_rLD%o)~q838&6fOhQY0Sv>et(wrfRCv}Xql@rm{2PHm2{Y0^<?+Oq@ZxuLppMDB*k'
        't{4OD-3{a2a9eVZ+zXS|Gi{9esp`vpaumkC>X_(=Q5gPHw=18M`*D+K%opt)HP5Lx)1Eva58_6%=6LC-gSZK8x(~_Z^Cq*=bE`-F'
        '!hhYOJk-dKEXmg!zwZ6TE$L6bAP?hKtNU!a4tkc3Zdo7lMR^3baBKZDqvH?jV~=lX-}0zDW<mzqifeXa%lnYW8==UC&Xa1GkY&rq'
        'Ay3GY2!rBldxY8)&DZzLw)HDd$<qkAHarhh>omf%Z5xw3BQps7;&mY6l`y{Ty~?w43_<2o%?Q;TLr}Wy<CEj^90K3g6?2-}9y6=v'
        'rDrx4d0tK+@P6t!quLV))}Pr}<xBEqBnHc?YfP`Ni_d%<@)dajNy(<>j#{{YWagQVTV9l}B7s_c9Zpam7xY?u<7XS6d`-TNq;Avm'
        'ORc<)gz#rO2l<A46Uk`Hnx(6cRLzoivX-5_V^e-X`|nalNy#7`wUpgqXP0a`_A5#*DKDh@UuU_U{o1BhzM(vmQbcO&+w7Q~{nn;F'
        'A5h9k*`mB8zsp{-v)|eBy8NE9Pf8r+l>8w(WoLh|<wx=%C8Cr=%3JbB`8a#arYto3qb-$uM2RWol$1@%vivDqwzEIka-s2%F-=KO'
        '`hO`2O6%Zvo0Fh)<MID5ISJAspVdi%wj~Lw&+V2cLHtR^x(!JXZ@muxw@DCRPF#O6NsvD0BlWA>NrFrg6t9C$60~{})Vg9iNzl_K'
        'L1uN0#p|n+1Z^@2itkFDB<NWrL3*y^h^9FST26rO$TSilN`w;2Sr9TH%7wNg3(`3dB|wiU5n3+`GJjQ||HQWS)2w|-%ThaMzayC)'
        'O+N9{tl{`i&sX~<Yrp;`>)KVW`@pwZWp}Yqa`RjG!T#*O6Et4)k$&TCxq3KR%gvrln(wQ|DBl}PH1;%JueWX2(~|iQ9K`=(wLbs='
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)