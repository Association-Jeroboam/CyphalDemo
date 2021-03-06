# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/physics/kinematics/geodetic/PointStateVarTs.0.1.dsdl
#
# Generated at:  2022-05-18 08:58:47.684478 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.geodetic.PointStateVarTs
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.physics.kinematics.geodetic
import uavcan.time


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class PointStateVarTs_0_1:
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
                 value:     None | reg.udral.physics.kinematics.geodetic.PointStateVar_0_1 = None) -> None:
        """
        reg.udral.physics.kinematics.geodetic.PointStateVarTs.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param value:     reg.udral.physics.kinematics.geodetic.PointStateVar.0.1 value
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._value:     reg.udral.physics.kinematics.geodetic.PointStateVar_0_1

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if value is None:
            self.value = reg.udral.physics.kinematics.geodetic.PointStateVar_0_1()
        elif isinstance(value, reg.udral.physics.kinematics.geodetic.PointStateVar_0_1):
            self.value = value
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.geodetic.PointStateVar_0_1 '
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
    def value(self) -> reg.udral.physics.kinematics.geodetic.PointStateVar_0_1:
        """
        reg.udral.physics.kinematics.geodetic.PointStateVar.0.1 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: reg.udral.physics.kinematics.geodetic.PointStateVar_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.geodetic.PointStateVar_0_1):
            self._value = x
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.geodetic.PointStateVar_0_1 got {type(x).__name__}')

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
        assert 536 <= (_ser_.current_bit_length - _base_offset_) <= 536, \
            'Bad serialization of reg.udral.physics.kinematics.geodetic.PointStateVarTs.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> PointStateVarTs_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f1_ = reg.udral.physics.kinematics.geodetic.PointStateVar_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = PointStateVarTs_0_1(
            timestamp=_f0_,
            value=_f1_)
        _des_.pad_to_alignment(8)
        assert 536 <= (_des_.consumed_bit_length - _base_offset_) <= 536, \
            'Bad deserialization of reg.udral.physics.kinematics.geodetic.PointStateVarTs.0.1'
        assert isinstance(self, PointStateVarTs_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'value=%s' % self.value,
        ])
        return f'reg.udral.physics.kinematics.geodetic.PointStateVarTs.0.1({_o_0_})'

    _EXTENT_BYTES_ = 67

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8N411v0{`ut?~mI?ddIc;v8$Ek^?JQ_6#ojH^V#dfE9<wYwAU)<Bz4MoW5h|$XfBZ`X}qK?kqSwzcdxiR<%%9`fWQe256FMe'
        'yz7g;3D7s{n<8irZC~c4Uj{AE7e#>vD2nzO>N}E_-gV+2xHr)Pt7k+GXNEKLnfcDcp$5_4{^PqL|IdA{x7V^;opjA+maca6pQ()w'
        'OV^raw`bbA!#wxsZO7_2oxa81-s>^%WADmG-p{=aH&!#$E}bu0Y&+d=S!yTU)Anq=X{Yb$2J5O04{kHF#VC}%W$K1=+fg0%u4=t)'
        'dv3h8!z^1j4NnWXOYb85v8RNTg<pFgdG3*#>Nu9(=sV2z-lrT7DeEMb=f+;sS*JBEW1`kl9ku50f@|UNK`rK9=&L(T)kr&fm!)s-'
        '8BNVH4gF`V^)?-_9ktu@v?Xm>Sx`c}BwCVk*H&@)iNng#v-Ga+=sQ%76Ym(dzHPA9>xRR&nYF*>j?@~uQ|mBe+tEBlrcyRl+o^S_'
        'rabMed+L@*h+mezPUmj&Q&cqzf9bvDx$8A5qtQ~W)@(u#`whCaBVD~|nKo;hM$2=fwU*iR?)+Og6na}@lF{!rm?fEarI}c^<Y=lR'
        'Y3dG>da7-+mSpQjlS#JOWs+)97M5!5NnQGCIFfEqd_Sg>PVhu=oDwxHeVa~i=xLU|>c`?0EHzY{U6FKKYO%Z2F<MfOS(|FF*U_8Q'
        'M@%Cv@no8P%i`%wF5x-#ZI+;hk{V31*oS>;8@l|iWp<~j+mq(=6O+1BFlJqqY{vXZO_S2Kdvv3^u}w#<9i8sYFN*Hxo}jy+!tJP?'
        'KI5fyOvzw7yqf6aZpXYoF5l#Qv9w85BHh<pR8H1Zsf;fr5|Xqj<vu8u_SY;$R~u&Ek#ae?DD5%Tvad?_HNC0vQ$1=qXD=<iER_m='
        'nlsl@x%<?2Ea|@4@3bf*%0ZI)hQXT5wpB~-?2U^+9YN9^ds14eHoA;T%Uh&KxjLHJw|Oi-dph0fQxcL&xlzJwSEu?i9O}nX)6#9-'
        'PLFTqdWZUg-rT(Y@|Lt=n2z+?D_11y2?o`rMfo*Vi#kQW$Lp&sHTDQno?}nl>zJzF#?(+WK&1VGzb%?d>hj`mQ)F9HJ00G_yt{38'
        '*rp$SoW)%>t*9=e1LHpGOxl4u#bt+g3tk5nKWk9KNK}b-+9MEF-1v3V;FvfQ?z9uyd4w(~vi7`oQ3-LLw98|3mfqP?w%+{7mZx2D'
        'FZ~&_%wX1jf1`HewQ<id?;B~)U99;9^4xP`P++?~>TrB8+czY{-}3vX+7ac^itaMqa+4qB!{KWP(|LCx<MEQ&jedi<CuYXMT4QfK'
        '?DD(V&`xW4ZL?1UN{dmZgcECd58aj8U456eYP_Lpddu5#kJoIoZ#5a6=&)K(rQyO|;-;fFJa_pP4fVUX_|cDPcv`qd1BYhvu|3?='
        'JvVWEuSae53hSDld#2ZK5V$oO^!pv2-*kkfn^+tVtaLrEE6+WD;NY6hrZZ_?S)Rj(vlBH<wW&}X{~7@G9#SLx)7BVxo`b}5;Jt<T'
        'H!T_scqQ|GOHiu>taIPA?rr)+*fV+hZRTf6J;l-X5k?7^o&I<X@P~kDKJ-P?w>4snYSrx00M|msyuUU~N{L1%F$(((?ob@l+O&JD'
        'so&LS`Z-My_gI>b#f=VC(IwGOrb9Q~v=jX9xyc{v&Kv&s+icQ_-AK*sd9HL=BKBUlVN&~0t=^>e!l3vj(WpA6HJySMYfX*t_q3n7'
        '$8M=DJ~loUNmKdRt$wFN!+-FsR{V{(p~yqKK@)jzoPwvs`whC!u5R#YjRNW}4=nMijd}}DR9WEHg@#HPHo|Rqs6_ES#_hsTS;X-r'
        '9FM~;<9LGG#i4Qp@sr%fhssfIqeEo{@sDwPWT>p-{Bdq$LuC!=oZxnCsH}6lI#f<_yE0Txahn_}&v2U<Dk)t5Eb={#e9j=9v&iop'
        'w`YdRd2UY+mFKv9cBn|)riRJ|Zl4({&vScfsQiH2lSAbqx9daYhuoeRDwj~M%iJCxDjO)@6>g6Wl^0OX7r8w;RIZ}Do4DUJ%6*O7'
        '<)M;6`Lo<E4V4`3Baiwh;C}pejSQ6%?yHRYm2rQSal0!o!Ttg4AHx0!_K#ry7`6&~1NIKA2D=OU0QM8uPhmfU{T%iS*e_wf8rz%k'
        '1q4zeupt7n2;2~XJ0hToz^({95P?rb;8PL!Oawj`fiFbhOA+`Afj+4_nh|Io;X^x)HTb|zGtROz)tgt`5TCdvDsx7z=D&r)9t&7V'
        '>41QpNjm)$Nq_THUwn#GpP1xXclkAv6V5*UOtW{DX78MK`2kgKSKTHd*XPptM|X+~p-{G5DVHkwY`!3ua`|kroRPDIVy;}s<;(eO'
        'IaA0NOXZ53DQCzQb49sOs8mYDid@N-3+0lW;n(C!nX;V8kZQ}z<x-|7SBgcsl+Tq*CAlnT%h_TfQ{YGQ#cUxj=L#iCzL3vl^SP2N'
        'SLkb2rpR)EvY`J=zL+l;v!#k$%200EOtD-l7PC1ymnoNWg<_$S$y73VxsuP(#f40nGLwrLxj>Qf`3j}YbIa%QC5n~H<tha^TPn&K'
        'xmc{^Dc4+{?v`$mZe7lma+yN5P$<*QQ(^N|+HzLTRI-&^r6SAOTrops&*Vy3xsc5jWJ<Rr`*OqYlX05WQJ+`b_<NSx(pBUA{ay3l'
        'A8QEhKjyXnUDW<^$27LTuKK5-Nm$6*db&>(q{mVq{S%Twx0`B506Vjeowwrep%r6YMr$x?LG54q4OM&j=UzKWwc3u+hpk<IsJ*hK'
        'y{g^V&|cU6R8zD!w42(N8@5SnM|m@nj>ekaJuz*{{i<2J{g5ZGy`$Y3>#_H=4<@p$ISFmgh_xz-HSHePXj+Gwyi5Pap^9uFpva<7'
        'WKk%xg@7VkfFg@Rku5`!MWM)&P-Jl^vM3Z;2#V||6j=g_Yzc}i3PrX6MYaw_wgyGE3PrX8MV5pjOF)sup~x1Y$f8hWVJNZ?6xnl7'
        'WapvC&Owo#g(5oxMRppB>{%$X6cpJrP-Lf|$WB6$twWKWfFfIiB0CO6whBdd42o<8itH#9SrUru2ozZYifkE*EDlAs1Vy$8MHYi1'
        'i$ak_pvb~dWD8JaAt<sc6j>FDtO`X|g(9m$kyW9{s!(KAD6%RPSrv+`3Pn~GimWOWSyd>qs!(KAp~$L2kyV8vs|rO{6^g7X6j@a$'
        'vZ_#IRiVhLLXlO4BC85TRvq@W-ytAmSX}K)r#$Bsov-Vf+_~f2XKd{5>X^i!?+=h{rb->Q!#dK&&D(EW@fUwQ%3VK7k82w42;qlR'
        '!(oP@rX{|>=57E<<iy=VJ7WhGCBj`6j1LnV+J9<aYX77CSNqRtsL=kmf8b!@Mo3?IZp>F$d?7#9ShP}~sw~fq3!UY;E56dA;UgOu'
        'K-|Co6GW1HcQ0wwmn0zou1b^1=&FC0qVQwCpJ{Q=3$2u!8m*`e?gyf*o7(u!cj<&5gD=og9b2!yB78zT0h<=+e!3lXkNe2{Sag{!'
        '{LMUZ_F<oDmD1)3TvsiJ*)$>Y(lURkp7y?O2>f7XHGA^9X>c!zap1DpT^_HBEoN|k^OI9+52=OxFYS*hbXfcY2H=JH06ZUn=L0Yw'
        'fFHwy*_@35u`zf88$owbB;YOzAL1^GgN>ztyXXkm2!oAyfQ{vVyJ!V$#KA@wY^;HeqXBnO1Z<?h#yZ$o1sh4Q5eFO502}AP#%Zwe'
        'Ou$`q9BizBjU!+q4mM(7BMdfP02>=%;}Y1o2sWMv8xq(!4>rz%jniNw1vXBBjdifG1~yi~#tPU-f{g^&h=Ywqun`3t;Q$-LU9<r<'
        'QeYzvHU?m005%3-V*oY=U}FF_24G_#*cb>l27--&U}GTI7zj27f{lS-V<6ZV2sQ?Sje%feAlMiPHU@%?fnZ}G*cfm&gjAo?FsI>r'
        'Pec0@iLCMLFd`mCPv9XG;2{hiLf|11;2{DY!r&nW9zx(D0Ui?IAsOI7JWNP}hcI|Zf`<rrSOpJp@DKtI$H7AaJVd}l3OuZVha`Ad'
        '4DfI!@G#*xcu0bWCGZdi4;R6M1Rl<UhZJ~N2M?>@AqgJh;2{bgLf~N&JiGuNE`x`Q;Nb#zI1e7qfQJ-#I0+usz{4@{kOU9Q;9(Iw'
        'L;^fyz{4tdxC0(;1Rf@AfQJ-#h=Yd_co>0)5qKC09!7$Pk>Ft@co+#DMuLZt;9(?q7zrLmf`^gdVI+7M2_8m*hmqi6BzPDJ9!9gX'
        '!<>dW4c~hj;K+%M_hO9wt}`39&K$CF%(B!y&s~3w@0J)pYJZs@+P_=tXpMCk-{ORAWK*~K>Wtgmjg^YUOaVS%?nzL4YEyUiJZ14<'
        '55-U2wYON0Ir_m*=)<*p{L=j%gw>&cryZqE)YqSa`h@`Xu>kdpfd}gG0QE6Yp9J-b0qT!{`bAK`5O|=T1od%H9}Q4{64bAO`eUFz'
        '3F?<Y{UWH31gJj`>d%7u)1W>D>Q90Cbx^++c%Z%l>XV>80qWzRei771L47zt{WVaZ2KAeu{wk<{5!Al`>aT$M4N!j>)L#PiKLqs`'
        'LH!Rv{qvyy0;rcjeG1gaL46(6*Fk+9)Yn0M9n{xBeI3--L46(6*9G-;L493NUl-KZ1@(17eO*vr7u44U^>smgT~J>a)Yk>|bwPby'
        'P+u3+*9G<UDfKH&b4MkvjV7!0Er;;GbBx5|d;UY14|4A(-s$ljhnBvrIg-O8Zg-gQNlvfj-b+j09s4GQH+1&=%nnA2aVIHv;F^*u'
        'Ig}!{(Dgd1!QHx++20;}La`x;wI+VmYZJF>I`QgwXqmW55A(hX&#Uyh^DSMj6Bl#)7m-j%d({4KGVNc|$H7kK_AmGot6%bu0sr`j'
        'fBcF*+~Z<5zyS{BuYV%-ln&JPL+%I{PSd&AnTwt8z1V60CW58#O=&^v@{ey$L?l2&@G(Lt;2a7EhzJKBBSZp3tb&LTh=>H7L&rcw'
        '7(^rkL>vVXVGywvc#I%+)~$hv<p2>W5U~m(;vgafBF=$`Qy}74z&W%4A})f6^B^JxBGy1e5=1Nph<Fi1TmlgnK*U)P@eGJq0})39'
        'j}an)opl8ekpU4`LBs}#xEK%uArO%Q5w}1@21KlahzB5I7er_v;tq(o5!hL`A&5u`BH|!|`X7++LpLU&JCl$$3GGfo4<?~cCZSI!'
        'q0c6v&nKZTCZR7Up|3<}%!ePEtc~Y*%<-7x@faRr*MrcwkFA$yHkdv6<u3nSjn4Qbo_ATt<m=u1%r?>RledXJ7udbFgCr=eCas0@'
        'PuRTH{)-62<3{_}T+dEd<<jh`{BpjK$;r8Vp;XGt#hfe`D{_`^V9Uz+f?VL+$#TU)A%k^$+oiOW$blNR{a4d0e>;x0e{n9&7w7ZE'
        '`FwG{e{sI*ufl7z0I%Vt#Mxbue;uPmWjS{EuE_QZUv~24yc-w8gXgYdfcQ3BBHKTX`3uVU9Mw6hb5!eJ>pg$MRC~Asd_0jZezS>m'
        '?&Y4-Ij8ffz1;50?``<A>$UOBdgX)M`_j|-x~ERz<BK%UUgOj8uXt!}@oD_R?va_5faji^T?^0*oeS<d{_qW2L#UP{X7us9xzpmM'
        '6K^*7i@;30d##UOrJrmKRy&g2Z}_k3(!CwFjF@?E!uzh>(ti`1aZAs~srfkdy&tFA=N9KXwC0a#=8tLSJGACB%xO4yht|}IGhSvw'
        'eO}^f>WlW@E|H+T9DDjL38(h`_Q63fx}CYrm^6*$|CUROIjY{Vzk6}`f03z+Y5ovu{t#;Z5bCjqP;FPJ#hZ^fAdj8~kWc`S=pi#?'
        'DDZ|$DDW<16o7;RfJ6f`WDJ0W0LWV44VU!*AhE!^kS7616o9M(kPrYl764=ofJ6bvvw<1%A^=GNkR$*J0g!V5WDS5U1>SHu4?xxd'
        'NFo5pWdL#>fSe4x3n_jcC<8z?0Eh%YQUGKXfW!ev2!Ip;NE(1#4git~yx}6=g$x0Z8vrB)K!yOM2S9ECkPHA>1t4DvK)w)wd@g3l'
        '&%_M*shA-@5i{fiF+=W(8B!B7<Q*|X-gxZifi}bpnG!Q(TtM+?0>z^V6p!|8T$m#<M?xSm+d&TU)Z>Q({#iTT{)af}j(>ex@stYu'
        'H0$qUTc=i=ERSSb9?86?Yror~dExJt#JrFS69n`jPEF_tp5V2T{(rbK8Wz=7000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
