# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/sample/frequency/Scalar.1.0.dsdl
#
# Generated at:  2022-05-18 08:39:27.442180 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.frequency.Scalar
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
                 hertz:     None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.frequency.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param hertz:     saturated float32 hertz
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._hertz:     float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.hertz = hertz if hertz is not None else 0.0  # type: ignore

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
    def hertz(self) -> float:
        """
        saturated float32 hertz
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._hertz

    @hertz.setter
    def hertz(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._hertz = x
        else:
            raise ValueError(f'hertz: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.hertz):
            if self.hertz > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.hertz < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.hertz)
        else:
            _ser_.add_aligned_f32(self.hertz)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.frequency.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "hertz"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            hertz=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.frequency.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'hertz=%s' % self.hertz,
        ])
        return f'uavcan.si.sample.frequency.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8zp#X20{?Ya>24gy5hf||)@e$zEZK6)aYQl^$GnzWIdL3?iXf-0wO~pKkwb%?ndWwbbEUh7<O&E7|41ML17rYo06&5s!H-}d'
        'LF}JKp1{Zx_-CqSdv-}#5+HrGeN<J~@zv<BC;xfn^ho`ud^_(&I*L7Cb0t|UpRyq4o*!mOo@r^gEl+P5RfMKc{82CG_PJgB%>KnL'
        'l;eKN64<|9u)UC_o|c|wNe;Jn6#sL<)3E1lg)C;umQ(&7S6XJN6(i;3Z=L+y(os6{cl((wXMJXjl0jj(wtoWcukdSd%9i8zB#)z^'
        'KQn&B4D$^-DaQJXVtnA9kqP&<dTA(Bmdd9*dISsFfX7x$is{A^aSE)9bME@wtNh57Or()};K$tKRLgG4qmNR<yIdWQ(ySjy<HtPh'
        '8ewT0ybPH(ev(Dt<(uWDhm9h<=54~>1Kh&U{LOx9%L_jEm_|%RM-?3w0X%Isk)g^o53@9~<w-xvLc9IHv5}ESf|ImJ0<K85Lynx%'
        '#0X}HV0)b8OluwyEz^(_oh6(w1tt_zJ(9rB)DW4%`TC^sW>BeH2c?;kUD#fb9`|n6r!c@IV45!ysY%3lB*cW|TrIIYk7dXV<lG~u'
        'CM=XfJ%cM~snC1|5=8<|>iW?JuJ5QU8EV&q^wr8p0*-NYlW5NCLtzGbbq)`eX%|-2o`kp6uE^T@47>uI+hcLT(Myw&l<#4f;Gdm1'
        '+wc1~*l%qtK}g8HjKEJGGVt;JnHfTs$m)~U#_`C)aTa8SA*-wH7U^-O^i8raWGHY8`XV(wkK7>}>$T1!cfs!hYDba%tcW8p1QrM>'
        '(v*i>Yo=t}>$?DjK%~(FZy{`O4ZOvSw7{wnS)uV%Z63Cx0#pzN)<7{okPxrbKpm4%NiDV4f6QhKwIIW#%{v{kkY<M5ySqrB5>kkz'
        '0(&7-P!vUu@w!EV9yBRh%vmqaSe;`?6p(>eJN~Fi6-m(jE*#c^#W7|W%dH#prTTc^#10<@D&eruuTe9|0~E!)!Lq;@DBMjUF$99B'
        'JqwL+rkvW$Qfw15=sPhdt~u#CZHsrryL1HmNzC_KXYz4}c0T!C$BM=B#_zexUNl|T8{`e6v72W5sb|Xxzjnx$Z#AUA4{|6tB(r0b'
        'F!gC&pDb?t5v_6>o*d$;hW&d^hW&DM*`jAUC<0#29pOPg==CWUU$G#rh&8cP0HH)2j6yr{$R3tw{2h6~BOepx%gA=h^S;gs6>`{!'
        'xt}wji*gbnmVqs&9|El(JjB)KKu@FZ0da^7d3-FFww&4Q<&dkpJjrZ%H7^2aTwn2S5u?2!!@?sb`os$NF;=#`_EK{7R=i~ogJliU'
        '*_<z!2B)z7eb=D&5R&k(PQT&N0znH{Eztj&0ye-PW8FeiGiX?|pQ+uYx+C-vn|01=qfjYE9P2Ppki|ux18NEw+JPTJb_MhpL^Vr*'
        ';38)j>ov$g6R=am!gUYs!I?}g>70jhM;@tj7!bSMLoN<t2+@tEPKMMCk2Wv<w&kf`N%L|2dy5Z>xIE!!xh=`7l;~a(WRM?->I2A^'
        'BgIdk8=1+}a0E^Gp@8<c;*aIohb%&F{J|l?aJN&$Fs^$q?uynw>;i39I)Fi*_cd5LRRr+PM5Z{_Kwt+bOyX#RYC)xR6z`2xbj;xi'
        '#IcH=bic<DM=Ltv)+gQil*4JaK7%+>(OGx?6yj7xPa~eJ=oxqZEaGfM&$<2ch~pJ~&FPs#e66Av5YJWgBI22fUP3%o(bo}YDtg)7'
        'f5X|m;_O^?dfs&Q-a@=u(QAlTD*86!8x<vpmn(W5@%4(ngLtW;KSI1%(RUFqRP@J)a}~Ye{F+BRU(p5U-y-7KivGm;`BTKx6}{>F'
        'U2^aBoZs&uPFHl<`M-iVS<zMZjx`sLb@!e+uO}+H;of!2#kcL=ce|f=`o6=TIsCc94;=o&;fD@?>F~b8ZHL0)fx~AGKX>?r!!I3v'
        '<?vgF-#Prgj}N9sop8Ak78;@52=^OdyAebq95lkSM)<rDzG#Fm8{w-)__h(gYlQEeP{7w6Oaz!CNbPPdKw^i9Gi`?7n~UWL4z9sh'
        'CVU7^--A(Vj(t1A<RUP+R>k}?P@J$Xe8d#^+4w;@zqY=-+Fo5--`H4dw^rNj*6sGn%B|(~mG;_td%d-?aeKA3zTTfKwfS+um3a!L'
        '#n&)r#2wWCA8}s%SA0{5%|mgwBYrLJFNlxCZv+(|iwB}pj%k<(6a9~Riv!Gk*4y%I|HJ+`xr?nsR4*Qj?LKY%K|C3-OE{389ATV`'
        'Ft~A&r7xwfa=Oo4Ff8!@1TWR*i(NVjFN|TzC-64~yZ`RMLiY%D5uh%v@z6FL+8!R-MHc(PGG@&CKjD<bDkTj700'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
