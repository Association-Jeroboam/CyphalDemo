# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/sample/voltage/Scalar.1.0.dsdl
#
# Generated at:  2022-05-18 08:39:26.777909 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.voltage.Scalar
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.time


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Scalar_1_0:
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
                 timestamp: None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 volt:      None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.voltage.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param volt:      saturated float32 volt
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._volt:      float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.volt = volt if volt is not None else 0.0  # type: ignore

    @property
    def timestamp(self) -> uavcan.time.SynchronizedTimestamp_1_0:
        """
        uavcan.time.SynchronizedTimestamp.1.0 timestamp
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, x: uavcan.time.SynchronizedTimestamp_1_0) -> None:
        if isinstance(x, uavcan.time.SynchronizedTimestamp_1_0):
            self._timestamp = x
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 got {type(x).__name__}')

    @property
    def volt(self) -> float:
        """
        saturated float32 volt
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._volt

    @volt.setter
    def volt(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._volt = x
        else:
            raise ValueError(f'volt: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.volt):
            if self.volt > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.volt < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.volt)
        else:
            _ser_.add_aligned_f32(self.volt)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.voltage.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "volt"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            volt=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.voltage.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'volt=%s' % self.volt,
        ])
        return f'uavcan.si.sample.voltage.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8zOaO10{?Ya>uwyk6_#XOSH4EJ<JgH!r>P~i-idB2uhXWfE7x$!cw@wNEA-+4XNFo5np;WEN*ka+^P`0Y4A22Q1@Z`aggiok'
        '7EOKzeS)A*ke@wghO?3!+kpL@B{}CDp38UWzfS)1!l|+9Pkt>O2092GS92v<C_iOh$Q{>DqBPOc@G?L3$f(RWnc|O!DKDRw%b%5h'
        'DVOpoH)av+U(49QXR)KDqgj-~*MlT9tk0cCJ`0&D^I3Pmm6l0dim`m=w^n{$(s4TW_wutcpLdxtN_v^$y8IL9euY<~Q)NDNPx3H0'
        '^rqzo%rMuWi(;Z)6jS+i>zt7h_%n=sp^{jB%7e$Spbhw2iWxE2cp^@Mb#c~yzVIqPQY9m4<N*9wcoJ*bk9qK6Y<Qom<1w0dJ!#yK'
        '$9*G8+66Ctri~jV0eJale(_<W2tRYSVDABLVQBtVep2S=UGOmum<o<6I><b@+I%E^m1yoKaZu)yZjkup_Wvfv#vTh!;w<vGBFPRp'
        'a!L~;m?44<I7yk-JRn-eJ|{YfIAID*D5i!af}gP=GKTZjN#nFosa*%9iIRQTUXl)XZdRu-z{F#kFB7Rrz;`6Xgrr=xS(=8@X9jZa'
        '5LDx5N}-<7Cuk|tyakCO9w&<bIfLB5=Q}Ei4z=r1`YL540>`+zNi^rxAwL1VI)#hMxDTspAmMJ6E3&fQf?I%d0~Tf+y)+4l`2fQN'
        '|LlaxUhUs#zq8qfkdQqYfS=rF;NyF(79nl2_O!EkJhE_{c}Zr-+FG|mhMXyVlk5rU3*3UPh|SO;cgW^OrSr(Q;CBYKqsU&8g#j1>'
        '3xs5G%zdskQ!*UZE<hm=Y4pfj2pfC`-eN{NVAY5u(|D>f58FWoDhLB>pqTGVh*xZ&j)||NmfEQ=vlT)uNWZ;xr$?6J#E^S;mkCrt'
        '46#&T&u0pXB1<t|w}>}{CPj-W8-@w1atw(ADsU>tA2+EY5xU=p!&<N~#0+D(^+VpSj@Kr3_+g+T4hwaSno%C0C>9Nt1;#+(ZVZVb'
        '5Jc^i&<LmV*{vkTHZh~V6AR+1m9EpScw4+f$FQHoV%<73PkOZX@$Y)2Sk7<!o~z_V(^b7e-Y^=wak3XXWj^gz4wd;^4Jq*b6bcT>'
        '>=-4?ep1yZ3mbn#C!d2W`?#uM|DKg$KObKy(KGF39?ut!@Sy7rYl6jFEQ!lvU9>YGlz@X#XeS<&2l;7tNAB~$#YDL>D0}%iS0|bB'
        'Ic$X7O&QQdK7$ZSugvEj0;%sm#MS3OPvh?bafk$2d?J-)-r5?bkgK~qO3M67nt9N;uHyYHM0<w}3zwL#i50%bSe5zJmy)Zq>Z~{z'
        'tkNKzEx3Yda0=VswGCPxKob7ds~a9I5VU~R0{x#TU;_*?)-5zOgN8MGiP~*f9ifldta4Tvg-S8vScidvB+P0Ks3_pj4*U?ZFQCUD'
        's!0R{7g)nsuU-P0fSno^u6l3)XA;%cDfi`$JW}T{Aa=QfT<nDqq8m+}98x!2+PwI?%uoJGnvbgAkNBvF^Am28mN|Kq5<QH(1o8t>'
        'eE|8gr1&v(BQuFQ96{5rFQENP@yGnkLlz)6{@{>cxZBG@7}vuWcSYwP<r3`{+Jix!)*4DWn|W~0NX9tUKw$eQ%;0E)YC)xR9KRbY'
        '=!C@+h!X{!w7;hi#|t`b*Jtedti?II-a?!%=)66D5^=Vmrw}I#dfJ{pgE(K%vv&U+;#5Ijvw9W~Un}T&#IpsxfOxu~7ZFbu^mW8m'
        'K`+_w->`NsTRT^*o;R(%w-B!s^eW=zf?h*>qo4%wQbDgHzFyF`5ib_>M~D{+`VQjxg8mqBp`bUcUyF$63c6(dTSh!n(4Sa8e~Ngj'
        'pf|0*ZF^tG`u#5ATtQc?|Eq{I1zofEShw-mu=lC*dZM74_FlJae7p93x9hyq_bmR*;?FI<Z}ArvKd|^qi}x*VTND=eEk3jOxy3Im'
        'erfS5i{D!O&f@nqKA0W1!lg!7YJ_eh+;4>KMi7m#-w4kd;qylLq7lAqgs&Rm+eY}V5x%!V2CqAq2rx&G+U=T$#10c@&K$lsm-8_k'
        'T%%VeJOt<N!6-Gy-i|Q22u!XuvG@!WN30Kzm<*qd@8^r_8!Kzwwe^k7&Gl|)t=sL~?yj!hTG?3bu5WZVI;)$v*E$;;^<=5cPvVmt'
        'EQ_yU%!oUv{y*ZJ_^<dT6I%!3ZcqGL++PwOir)w-J`xW^FQ3pb5T@%FJ&X|hrZ4j|^{f6kvx`Rus9Zb|+cjtWK|CE%i$9W{9-*5H'
        'Ftu@v#V_Tpe6FS~m=yRQf|qJ@#V#F(>xD4lBlsJG-GBFBp?`$82=ErycxW3AZ66-mMGE`DGN#M<KXb#M&mau|00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
