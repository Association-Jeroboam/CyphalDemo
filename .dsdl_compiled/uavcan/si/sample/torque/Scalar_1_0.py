# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/si/sample/torque/Scalar.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.479226 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.torque.Scalar
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


def _restore_constant(encoded_string: str) -> object:
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
                 timestamp:    None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 newton_meter: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.torque.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp:    uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param newton_meter: saturated float32 newton_meter
        """
        self._timestamp:    uavcan.time.SynchronizedTimestamp_1_0
        self._newton_meter: float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.newton_meter = newton_meter if newton_meter is not None else 0.0  # type: ignore

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
    def newton_meter(self) -> float:
        """
        saturated float32 newton_meter
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._newton_meter

    @newton_meter.setter
    def newton_meter(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._newton_meter = x
        else:
            raise ValueError(f'newton_meter: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.newton_meter):
            if self.newton_meter > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.newton_meter < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.newton_meter)
        else:
            _ser_.add_aligned_f32(self.newton_meter)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.torque.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "newton_meter"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            newton_meter=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.torque.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'newton_meter=%s' % self.newton_meter,
        ])
        return f'uavcan.si.sample.torque.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{?Ya>u%k~5td}@F5e>CaqPrdr>P~i7NgsdkJF~DE7x$k@v#vrsaiB;m*nc~!X%gFE+w4+1)3i%Y=A%rcnjna@(6i^'
        '07cREUx2<q&?m^x&XCI^$*~1U-*7K8voo{btp0NH?+d3!>Ywt>Y!K-v_I%BA$zu5_3u5m1p-M8PrQx<b^~mH!Xo{R~4>E3_*`?3y'
        'pY38f?x!q)`Ktxn3t8%E>1mc^u-mBoPX+fLg)C;dEvNiFo@=R6D@Mx6kDdI?(os6{H~X0_XMJW&E`!2wZ9f6kFL7$P%9i7IC6A*+'
        'XJ-6}8Ri@GP>eN$V!XWOd^0iue+FqNa+S(Yd9)1!+JL)OOp58&6EO$Y#aXv~{$+k-xlE*yd*H|XN2!+mlt=HUhWB}XJVdj8AdMgM'
        'v~Pr^UGOqw+W3izz{}Umiw|2xxXs&wx%)VUq4}%*(3a<Y@G*^89vxNmv<Tp6vxy9IrFp2*$d)JlNQHLie`6yf+k%s{NCKV{wM&ky'
        '(!>a6h+uo1WK3%w5iQe@6Ri?XSPmv~mJdh*pQ#}-h4uAH<ISK_Hx5cwF8eUOC_V1os8?ZtNx(E;B2trx?@EXX$#}lZvMiP%GmvwS'
        'pqjAAbJR23f|d%+XCP4|;3VfzJleqa-CQMy+VwDfwK9@`V?4h>H0SlAP=Q{Z!9iu(htYgb!r5w9WNm#0P65vCvAE#qrBNj1dl)A8'
        'vm2}Z#=qfwXLA`sLiS|@e)5okkMGXR5VB0x{?OSx9$8q<0#z8Yw$|;C0cW|sLH30V1x~@GNX@__x5?&4t@FrU@VkK8$;rMd;s^|Z'
        '1wx86<ssLa<uV>LE<hm=Y4p%r2penzZ!sesuxf-VG_I=6!*o=D3c|n|DCP$e;*}bxV-n_4OYJp>*@~eSWVpO_yGIsNWysw-O9Uz*'
        'g;?fbFJw6sMUi2=ZjxXCmlQ2#Y!E9}=NJ+NOyJdyZ?~x;3A*2h#agg9#tdV*^<%zVFK<lj^20zS90r;iHN!kWQ7jlN3yeXIvneEo'
        'KoGTO;Ub(ar?ymz*Tf9(otPI_opg<M#arTSI)e8}EHqbV@}nN@J@`$}ily@U?|81BH(l2o<PD?oI92<pXUhq{cF2}*w4}ffGAKAC'
        'vtyJn^<iC~EN=Y~opKtE9O9^k`MXYr`Eqo{qGviN0$$D^;XywbH2jLESQMAVx>zoNP$CXS;X3iiJ}poCyYhfXJ|@bSk?ob|e65N+'
        '<S-F)KVv`_<s?EZ16xi%1WrGAh@;Pdo<`pR;t&c+d;*FGE|e`#^rf-o%+?@-tli;>vgMVm2;d6)Iqw%ST0Z1j*f7yhENH^0K|6RM'
        '&3dceiicsd28nIn7fgeDNCdvSs`e?Q;~%}|>Z1jM7O-xB2~-ZefZ@gphU?AX>Y9C(KVGiyhCX7m&R%U4YQ~6TcMTM%xM<j*CWAve'
        '@F8Shz-@#0ssyMma)z;T0|lCZr&>O)Z{r@UQTejYcqn(}k&1^_@tAwa%0Ubvy53gIA&JAG&GX;3ocpCTAJpHE_^_PI6TZr9NnWNz'
        '50XGZejuv%AzzLjAHcn2(1;J4(S#ogAOb5sDbGA)5whg>7Ks37dqoV5d+_|M=zMM$X}8h=wDhdeVChs5z&R6{VuJ&L9iT9YO%AFB'
        'mC{k%H&W3thbIunDtgj=k0Xv&bi$2Ky74K8({6kQaiXHLZv7nMR7FoAo~-C;xBd*`Y(>wy`E!Wl6@A6&nMZu3qURCMR`dem>55)N'
        'oU7=oh%*(v<o3Vj>|S<ut~fofJ9}>+Ua9C+#LE?Z6Y;f*62waty@vQ|Mc+caSkWIKUa08Xi03Q%L&W)tUUz;iAfBt}qVsPF@k~X3'
        '<ox_G;;D+>aQ-g4^LozjcMzv5y5js_MVzeYnmfn3i^qmLPo38j72R~_y6NKEb?3X)<ek3j@Fxy`>hL{>KXdqVhre)m&*6?k;qbuW'
        '6Ng_o{L<l94!?Hzjl*vpe%IjrsZl3fYK6sC=(fVWR@i9;(FzBx@T3*KXoW9Z;j32ox)r`@g>PHoJ0}$I&V$|n9R*3=jRi>Y(0iuM'
        ';mdQW9KjYgd~d>&aQZGZRdehW2|bKJ4_gxpPe5_P`tY17@B#T=xv;*mvesQ&-`Lz-?{?O@-OjD<>gvsvjn(e@Mt7sLx_N7@v$4_i'
        'nA-eY%J+>*{e;8Y0Xz`@hQ=dqqnUq+bK<|^KZV$OD(>{euf)AY@xJ)ApyC5@U-ZO-a!gC$`{t34Eu((s+wx5F&_7P`V*4p-7axn?'
        'HstYp;SV_`8cO~V-njsc96MY3LINwN8~%cpf&U}CP}?6xOh@6I33UAweihjLXAcI%5dtGXU|i#(9ayw;xF|+0``$3-&HF!+4C>`F'
        '4FCW'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
