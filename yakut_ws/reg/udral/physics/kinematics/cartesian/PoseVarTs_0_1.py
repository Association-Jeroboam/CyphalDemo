# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/physics/kinematics/cartesian/PoseVarTs.0.1.dsdl
#
# Generated at:  2022-05-18 08:58:48.189597 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.cartesian.PoseVarTs
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.physics.kinematics.cartesian
import uavcan.time


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class PoseVarTs_0_1:
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
                 value:     None | reg.udral.physics.kinematics.cartesian.PoseVar_0_1 = None) -> None:
        """
        reg.udral.physics.kinematics.cartesian.PoseVarTs.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param value:     reg.udral.physics.kinematics.cartesian.PoseVar.0.1 value
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._value:     reg.udral.physics.kinematics.cartesian.PoseVar_0_1

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if value is None:
            self.value = reg.udral.physics.kinematics.cartesian.PoseVar_0_1()
        elif isinstance(value, reg.udral.physics.kinematics.cartesian.PoseVar_0_1):
            self.value = value
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.cartesian.PoseVar_0_1 '
                             f'got {type(value).__name__}')

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
    def value(self) -> reg.udral.physics.kinematics.cartesian.PoseVar_0_1:
        """
        reg.udral.physics.kinematics.cartesian.PoseVar.0.1 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: reg.udral.physics.kinematics.cartesian.PoseVar_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.cartesian.PoseVar_0_1):
            self._value = x
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.cartesian.PoseVar_0_1 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.value._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 712 <= (_ser_.current_bit_length - _base_offset_) <= 712, \
            'Bad serialization of reg.udral.physics.kinematics.cartesian.PoseVarTs.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> PoseVarTs_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f1_ = reg.udral.physics.kinematics.cartesian.PoseVar_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = PoseVarTs_0_1(
            timestamp=_f0_,
            value=_f1_)
        _des_.pad_to_alignment(8)
        assert 712 <= (_des_.consumed_bit_length - _base_offset_) <= 712, \
            'Bad deserialization of reg.udral.physics.kinematics.cartesian.PoseVarTs.0.1'
        assert isinstance(self, PoseVarTs_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'value=%s' % self.value,
        ])
        return f'reg.udral.physics.kinematics.cartesian.PoseVarTs.0.1({_o_0_})'

    _EXTENT_BYTES_ = 89

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8NVSAw0{`us-ESLLdd4YAlqiapWql-y>^S4ZwPnZR@|(kS(>it5^>)?@n>bmm(+zh>j&(*RXV{scEd^bGd$ENL3{V1@0>12J'
        '{)F5u?`mKdZGpY0`vvr(7e=poQJ`tji@s<0oDp>_HSrec6$O~@;e4EP=HvG~?>Ri~&;0q^cVpq7|3>$q<+j?Hx@$P5-Znqi8*L*~'
        'Z`z%%?V6qu_@_SdoL<xGImVrXt`U3@T=`k>(_qt2)GfV3`?HR*o9VS2y`AZ@1J`W2nfs<?baamwo4Vr}uBls@n(Z2&=*}HC@RRii'
        'hU1#H6|k5;_X)~h1X@g+`qSWNfxl4KJ<l;4Jvuk|F*SBVH>0BhKXKDE+O5OxrRpu+)9W7ZGmDQlvV?!3r$1;?Z#=VOWIj5un#{2+'
        '^K+whhc>vL-suKxj?HURT8#IErKxqcgwt0}>POcxJEmtopnj};Y`NyHWwgF;dB(2c9KC4^^@i!y+lIC4u|QL)mrdRE>K(g9y*%f?'
        'QWF*N(=s<`-)+8&Zq3xsgAW6LwN8DsTDsF3ujp~FL6^4BF`EwE<fd)40)M97vYWxqzs6&+JIqk5UZ-I=ihWNRJIYl&rh5w09~eqk'
        'cU_~UxTe)K6xZ$;itbPoj_w>N9r|i{ifPgD;gMb@#Vf^js?>JOUD~~AW{k|W@F;$Rm4@ybR}|A#TE;zkCt6C^aJKYrw{14*^{}ms'
        '!mDZa9EaBvox)q{xkic}l+rL1$N1wOJsUdxo?~|oYj>l^7gnZpsAGn6O>qq)Jg8|?y>6E-)U<YKtMkC5YYV$#hOMXQDyVZ0^mfnS'
        'z4UCwG9K{TL?8Fs_QO&CqWz`v7Tpr%q1mE-8cm)0_)aRNC|gSYvr_r!ou$L|hTZd&d|oXn2Zrvr*OZ6MY%;#9OHa-_$SChA<ziUp'
        '*tyj29=$t`^3d+JThtJ>peQ}dGMa|#>W<ky7<GYO1jY2+sJC?6=rrmre<CGn)nj(g<wu3h)9zM}s!()ljVd<wO}bx}NAI!HbWGQD'
        'Goy>S(WZC7Y;N6nZ(G^4Y)`rQ{uPDZ1dHyaL+ugM^iuS?{C-uG#sNXfTkPrwZCekYF+C{KhD_M;JK|9(9p3$2I@o1;yUm|4f8BQ5'
        '##VUvsEK>V;f?ATv|;p)deL*Bm*TR=UkiQ@9KP402cytUbTa{gu;?dm*cQjci@0Me>^w>rG?l%{E^0B(6T3V@XYS)|ZTo{CZU^j&'
        'f9bB_*mBe1`$o@=-;Mj0{m{w;{%k$$P~g8VM8Vka(hJAM?1&^JKMdbby)F8~O8z`ua+7c6a(EME+V4+g1Ku;Y(Q6p~%9sw;8wVrB'
        '<yW!EHduje^+-@!1~p1J8Li;4zgWL#?i;N-e^7O^6>R%w>aN{$ng;D?8}+VEa^cVM&^8-^KToP`?$`L%FG!xIzC*&nY%c5Zt{M2L'
        '8wXu_R__}fJMhnTdkq4&PI}*K^Y#uEmM&s;B&>8kzgK~O{#bF%<TBX|zgdCD<!q(SbeB5C@vj5W;4wXfUv7_p=Pf9_1^%`W|F%PF'
        'z;7~tZwYFhfb|~Q&i$>B2zRW_@R@~;(wpM3BZN@}cDpyyfKUPs+o3Pa+-1ZV-Br6o0@p&r{C#cMR1>L_P~nil2Xu_>Y`I;dY2Gu('
        '-g7dD`$mRqaidMQ=#qF(4yBte+LONre){)J?+4-ckBsOg_NVK1H}I8{Dsc}w4V#`1-PPOlyda7n5RJNLJBJoDTW>PLKVX04pRVaG'
        'u8l7o#B{!QyVq`${L6b;>Cb{qO&z!mGV<=IhCoa98g!i<)8e*91%00v=D4-d+rlf=ruccWffh%c<}p6dX7D}1<J3T##r8RDPa@7^'
        'dy2=|fwq9-(>x{z+9@7q2HGNyKh5L9KwHB8Gdv~++A``{;c<DOt@5}u(AIcd9B8lbm>y`a@|YTE>p1^4w7Y?J&Z3@kXzz6%&knTn'
        'JZ=oMH+Xz)pea1A53~zBzB<s}<nfh(_7;z81MMP@s{`$~cw8B1m(Z`vJf0b7o9N#a9#0RntLW$3Jf0e8*U;ZBTyF;b{tl1x11*dG'
        '=XjhOXn9;m0r#Vb>j|Ih^gt`)x+=K8Dz2|OdhXggh`){aUBq`0e+Th*5w9cOLfk=Qi2I0-5T77^iTD-bQ^aS8&k?^K#oNg#6xKyy'
        'QxsHDxFrfZqQFF9UlbmR!V^*WQWU-tg{PwMOcb7r!q+JDD7zy^ARpn<j%^Jt?BqD}-eJCZ#gB30in7eHbT#vG$@M6AMHVgPu4A>n'
        '{Svi)%POyZ>nbTpd7;i@s}!laYi4?suw_PKm-!(H{U=6~1gY>ssy>#fpFLs3;5hmL<<U2}O^!77J-+E^ntrNov<;ryV*GH<pT9}D'
        'jd$cIN+qsSDv@WGAJLQU=)2U(9?#?7-6>7QV!2ASQmz(qg`!%{7jmUaR?QVl`ARWgs1$OQY_U)(SE_2ZlBHP6m(*ghS}m8VYBg6W'
        'R?2FYpOY_VD{3}NDP%#dl(QwZS}LjKLcUTis}(g@$(4%PBHvml<%$J0Uo2Dg#X>$;$d^^MN?&s-9jq3q3Hp~UlnRwnu3S~iS!ykp'
        'Emg{;QZBFNvz2nbSSnVt*=n|+RttGLxtOg`V`?d@7U`fup-Of0)(ZJTnU2cm^VOo7E0@%)S}Iiw)M~y!S4)>jm#*f^`D`&)ELP~^'
        'sj~&@Z6&8>tGQ~vT2<9tzLcfDXY=KpTFm8(D%D$7!`z3QWS+)FUA<{~2Z1)tK4v>3=lPU<HfB)E9~xc5Gmp2qc>O*<RcE_nrgeP~'
        ';@8%OtV92-6J04Lxl$ai6oV^GORh8xSBk@x5^$v$Tqy-tO2L)VaHW{!N@=)K9IljxD^0_dmf%WBxKa$RbOx@Jf-6nKmDb@(%W$PM'
        'Txk}r6oV_Bm0alzTqzA#nu9CF;Yt_bN(x-*99(G~uCxkQT7oO3;Yvxk(hOWF23OjGD_w;vU4|=NgezTuE1iccorNo{!<E+HO3QGi'
        '({QCUTxlMzGz(XnhAYM3N?Ewl5?pBqu5?RsrA@ffI$S9UR~o{VhH#}JTxlp=X((K2C|qeMTxlp=X((K2C|qeMTxlp=X((K2C|qeM'
        'Txlp=X((K2C|qeMTxmGyv0tGetSHejXxK<L#QwV1(Aj%G4fgJnezAXZ*^S5S{cZL=c59P;pZx*T*bmrkw(ZAV8XL@TQKq~fa}fUO'
        'm@pqr^Vvs_dF97r+!Up~Y2N64o=8prod7xk^bpX|Ji|Dkf6G~UemtQ5H05G}p9r%tKG+}SV>FsS%*bfuALV3$zZhm^gltZN*1vi~'
        '9HlgE+o7SJj@cev>GG4p!7w>B4RgPV@7{#(3EvaGU*tO({?row91<da>}co>X*8tsiPOv<_J~Kv3eP=pEX4jDrT<|684X<&3|-iN'
        'vv>W=1xmzK8ab591+|n{RT_rm_!uRpQbJ$kBZhp5#sf&t_hN*yHghcSd$Y7}^kr{;blA}xToE~VpCq9Fzes>QGc+yD48>2F8A?I|'
        '=A@aS1xP>~5|ET6U|yOTT7(27Apvnnz%nG@lr%Fm4GCC>1gt^=mLLIXNI()2Fe6F8>yUsANWiPo%+MJ~z#=4I0TPge1SB8<aY(>b'
        'NWdl};1VR@A|&8VNPq$fI1dRp2MO4K1gt{>UV#LxLIRc{0ZWj8MMyvz5|DxfBq0H_kboITKwOdlF*CFY30Q{&Bq0HPNI)MF(1!%{'
        'Apw0zKpzs&hXnM61oVXj^o0cUg#`441oVXj^o0cUg#`441oVXj^o0cUg#`441oVXj^o0cUg#`441oRIjVCLce!RJRD{ul9BZ0`g5'
        'I4KL?>kwUg7Jc}MPz(Zp<xmcOqYV6Re9WOIcuw$~;5ou`!FEi;^7Jv2HaMl5dp9{U|Gal)nppgOD))}1b?@&utAEcw{(*n|Bmej('
        'j_xTw$9hcW{f)35nF(9FVO#tsK<n7weE4h{|H;QOEWViHSoHs8lAKSH^GR|(mYnbXCE;wi#KZ0DQ>?>3zP%a7Br{A%L?l2&?1W!2'
        'lOQ4uA`%i2iy&eVL@a@b7>GznzhbUQX1EF>k|5$$5RnEEQy^j$M5H7l#IKl(AR+-G6cDivB9=fz5=6v6#03zs0U}nUUojIP;u?s!'
        'B$?p`h*$*?iy$HiBH|z-4<fce#3qP%3q+g;5wC%WRS<C+M5I7OLLx$ue#K0Jh#H8<f`}y$@dQLX0ulQlf`Nz~5OM2;UokfY5$l48'
        'B#59l5=ew47M1p+(xa&KBr1IwmA;BfPovVasPsH4eJx5OI>J&zn8gH+2^<qRBsh+nxc!Ftn5FUgm_)f$$`+5zwyb@-*_JhFwq*&k'
        'Ew^hN)7sQaWOY+gRu?-Vs}n16W~HodL0XA3D`9#{%IZ!@D{*4LbQYK{N?F~4G@wgMD{;;M(^+7;0Zf;G=`1ikFRjE8S=}@+Re<Tb'
        'v=S!?Ok=?GEns>Mn63fSMPNE7Wp!79=|y0AUK-FX1Jg7xot0MN6o6?4m|g*<7lG*;z;pwct^v~}DXY6B4d{LXOs@k|1(?Qw=@Vf3'
        '2$=2zQwB_T1g5uMSc$VKFkKf}T~bh5izux{l-43jYZ0Zjh|*d_X)U6(7ExM@D6K`5)*?!4W0Wp7?FYJJ>Q>XJ_Z*LK-T5`4^l_Ij'
        'R(8x?<|!WEz1ueU4<DnI#o`R5qtnj)a2fCmf1i$4HjY-q{y5qi4#t$thTS^2f_?JY;ZoT4Xj!w~w)slOebeQ89NWX@aCI@?d`#0j'
        'h(AKSd(w94+_$%0?k}~Yh{<by`k$nJboBdS&7IHk%5i_4tB&4E-Ic1@IlN9(d*r+Fjek_>XL+jj$Z0_|Y`;50!`)|lzofAD>CDRy'
        '+n2E5>i;%!->XbRz4zXs(n(|U>~uIbpPHmwlXPp6ZXJ_u?cJLZL-j$N@SqRtH(qco<B^oo9C_Y)R>EUJ!XpJdlE5P+r8x;{-a384'
        'g5z1>k(BUQmKGc*q%=p&Tc?1>2JlD%kF&rd1w0ff&522PEJ*X#8^9wCJhmh}R-^^T*MNrtJXV265_l9OJYJV3ujZr$#~I*p5qNA!'
        'X--m_w^pPD$6er&mGEHFg5#t#dG!}B%v=9N;Bj5xp@=jmCg@NjIyNIZ)+0KSf)4F#F@g15Okh0|6If5h1lCt#0_#gLf%QaSF^G>3'
        '(I-$$pqM~0g5tQL`6wx5f5p!1{a1o=t-pEMbZ|NP&#nI-2_dUTztpI#L;r|t_N#63!Cyx{_>?36G#>4Wv_Rg$??>i;0KE(beiA$Y'
        '00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
