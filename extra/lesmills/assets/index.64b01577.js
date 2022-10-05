import{o as u,c as d,a as n,t as m,F as g,r as y,p as I,b as w,d as h,e as V,f as v,g as k,h as f,w as S,i as R,j as P,k as H,l as L,u as b,m as O,n as $,q,s as E,v as M,x as F,y as j,z as G,A as U,B as z,C as Q}from"./vendor.da55cf35.js";const W=function(){const t=document.createElement("link").relList;if(t&&t.supports&&t.supports("modulepreload"))return;for(const r of document.querySelectorAll('link[rel="modulepreload"]'))s(r);new MutationObserver(r=>{for(const l of r)if(l.type==="childList")for(const i of l.addedNodes)i.tagName==="LINK"&&i.rel==="modulepreload"&&s(i)}).observe(document,{childList:!0,subtree:!0});function o(r){const l={};return r.integrity&&(l.integrity=r.integrity),r.referrerpolicy&&(l.referrerPolicy=r.referrerpolicy),r.crossorigin==="use-credentials"?l.credentials="include":r.crossorigin==="anonymous"?l.credentials="omit":l.credentials="same-origin",l}function s(r){if(r.ep)return;r.ep=!0;const l=o(r);fetch(r.href,l)}};W();var C=(e,t)=>{const o=e.__vccOpts||e;for(const[s,r]of t)o[s]=r;return o};const Y=e=>(I("data-v-1a5c728e"),e=e(),w(),e),J={class:"album-release"},X=Y(()=>n("thead",null,[n("tr",null,[n("th",null,"Track"),n("th",null,"Song"),n("th",null,"Artists")])],-1)),Z=["track"],ee=h(),se=h(),te={props:{release:{title:String}},setup(e){return(t,o)=>(u(),d("section",J,[n("h3",null,m(e.release.title),1),n("table",null,[X,n("tbody",null,[(u(!0),d(g,null,y(e.release.tracks,s=>(u(),d("tr",{track:s},[n("td",null,m(s.trackNo),1),ee,n("td",null,m(s.song),1),se,n("td",null,m(s.singer),1)],8,Z))),256))])])]))}};var oe=C(te,[["__scopeId","data-v-1a5c728e"]]);const x=(e,...t)=>{const o=location.origin+location.pathname+e;return console.debug("request api:",o),V.get(o).then(s=>(console.log(s),s.data)).catch(s=>{console.error(s)})};const le={components:{Release:oe},props:{src:String},data(){return{albums:[]}},mounted(){x(this.src).then(e=>this.albums=e.reverse())}},ae=e=>(I("data-v-d939aaac"),e=e(),w(),e),ne=ae(()=>n("h1",{id:"page-title"},"Les Mills - Body Combat - All Albums",-1)),re={class:"album-container"};function ce(e,t,o,s,r,l){const i=v("Release");return u(),d(g,null,[ne,n("div",re,[(u(!0),d(g,null,y(r.albums,a=>(u(),k(i,{release:a},null,8,["release"]))),256))])],64)}var ie=C(le,[["render",ce],["__scopeId","data-v-d939aaac"]]);const ue={id:"app"},de={id:"nav"},_e=h("Home"),pe=h(" | "),me=h("LM Classes"),he={setup(e){const t=window.location.hash;return console.log("current path:",t),(o,s)=>{const r=v("router-link"),l=v("router-view");return u(),d("div",ue,[n("div",de,[f(r,{to:{name:"Home"}},{default:S(()=>[_e]),_:1}),pe,f(r,{to:{name:"LM Classes"}},{default:S(()=>[me]),_:1})]),f(l)])}}},fe={setup(e){return(t,o)=>(u(),k(ie,{src:"/data/bc_list.json"}))}},ge=Symbol("Global Data Store"),A=Symbol("Global Data Store Update"),K=Symbol("Global Data Store Get"),ve=e=>e;var Ce={props:["defaultStore"],setup(e){const t=R(e.defaultStore||{}),o=P(H(t)),s=(l,i,a=ve)=>x(i).then(c=>(t[l]=a(c),console.debug(`state[${l}] fetchData:`,t[l]),t[l])),r=l=>o[l];L(ge,o),L(A,s),L(K,r)},render(){return this.$slots.default()}};const T={path:"/data/class.json",key:"LMClass"},ye={key:"LMReleaseData"},B={key:"LMAllTracks"},Te={[T.key]:[],[ye.key]:{},[B.key]:[]};const Se=e=>(I("data-v-6ac17298"),e=e(),w(),e),be={class:"lm-album-release"},Re={class:"lm-release-title"},Le=Se(()=>n("thead",null,[n("tr",null,[n("th",null,"Track No."),n("th",null,"Song"),n("th",null,"Artists"),n("th",null,"Duration"),n("th",null,"Exercise")])],-1)),$e=["track"],Ie={props:["release"],setup(e){const o=e.release,s=l=>l.replaceAll(/[\(\'\)\’]/ig," "),r=async function(){console.log("copy release tracks:",o.tracks);const l=o.tracks.map(i=>`${s(i.ARTIST)} \u300A${s(i.TRACK)}\u300B`).join(`
`);await O(l),window.alert("Release tracks copied!")};return(l,i)=>(u(),d("section",be,[n("h3",Re,[h(m(b(o).title)+" ",1),n("button",{onClick:r},"Copy Tracks")]),n("table",null,[Le,n("tbody",null,[(u(!0),d(g,null,y(b(o).tracks,a=>(u(),d("tr",{track:a},[n("td",null,m(a.TRACK_ID),1),n("td",null,m(a.TRACK),1),n("td",null,m(a.ARTIST),1),n("td",null,m(a.DURATION),1),n("td",null,m(a.TRACKNAME),1)],8,$e))),256))])])]))}};var we=C(Ie,[["__scopeId","data-v-6ac17298"]]);const ke=(e,t,o=!1)=>{let s=0;for(;s<e.length&&s<t.length;s++)if(e[s]!==t[s])return s;return s},Ae=e=>{const t=[];let o=null,s=0,r=null,l=null;const i=(a,c="",_=[])=>({title:a,prefix:c,tracks:_});return e.forEach(a=>{if(console.log("track:",a.TRACK_ID),!o)console.log("is first track",a.TRACK_ID),o=a,s=0;else{const c=ke(o.TRACK_ID,a.TRACK_ID);if(s==0){console.log("check prefix length:",c,o.TRACK_ID.substring(0,c));const _=Number.isInteger(+o.TRACK_ID[c]),p=c+1===a.TRACK_ID.length;s=c-2,_&&(console.log("isLastCharNumber",p),s=c-1),r=o.TRACK_ID.substring(0,s),console.log("prefix match:",r,s),l=i(r,r,[o,a]),t.push(l)}else r!==a.TRACK_ID.substring(0,s)?(console.log("found next release:",a.TRACK_ID),o=a,s=0,l=null):(console.log("push track:",a.TRACK_ID,"prefixLength:",c),l.tracks.push(a))}}),console.log("all releases:",t),t};const De={class:"lm-class-header"},Me={class:"lm-class-title"},xe={class:"lm-release-search"},Ke=h("Search: "),Be=["value"],Ne={class:"lm-release-list-shortcut"},Ve={ref:"listContainer",class:"lm-release-list"},Pe={props:["lmclass","onScrollToTop","onScrollToBottom"],setup(e){const t=e,o=$(A),s=R({lmclass:t.lmclass,keyword:"",releases:[],filterReleases:[]}),r=(a,c)=>{const _=(c||"").trim().toLowerCase();return _?a.filter(p=>(p.title||"").toLowerCase().indexOf(_)>-1):a},l=async a=>{const c=await o(B.key,a.all_tracks,Ae);s.releases=c,s.filterReleases=r(c,s.keyword)};q(()=>t.lmclass,async()=>{await l(t.lmclass)}),E(async()=>{t.lmclass&&await l(t.lmclass)});const i=a=>{s.keyword=a,s.filterReleases=r(s.releases,a),console.log("search:",a,s.filterReleases)};return(a,c)=>{var _;return u(),d(g,null,[n("div",De,[n("h1",Me,m(((_=e.lmclass)==null?void 0:_.name)||"Les Mills"),1),n("div",xe,[n("label",null,[Ke,n("input",{value:b(s).keyword,onInput:c[0]||(c[0]=p=>i(p.target.value))},null,40,Be),n("button",{onClick:c[1]||(c[1]=()=>i(""))},"Clear")]),n("span",Ne,[n("button",{onClick:c[2]||(c[2]=(...p)=>e.onScrollToTop&&e.onScrollToTop(...p))},"\u25C0\uFE0E"),n("button",{onClick:c[3]||(c[3]=(...p)=>e.onScrollToBottom&&e.onScrollToBottom(...p))},"\u25B6\uFE0E")])])]),n("div",Ve,[(u(!0),d(g,null,y(b(s).filterReleases,p=>(u(),k(we,{key:p.title,release:p},null,8,["release"]))),128))],512)],64)}}};var He=C(Pe,[["__scopeId","data-v-7ad375de"]]);const Oe=M({props:["classId"],setup(e){const t=$(A),s=$(K)(T.key)||[],r=F();let l=null;s.length>0&&route.params&&(l=s.find(_=>_.id==classId));const i=R({loading:!0,currentClass:l});function a(_){if(_.length>0&&!l)return l=_[0],r.push({name:"LM Class Releases",params:{classId:l.id}}),null}async function c(_){this.state.loading=!0;const p=await t(T.key,T.path);this.state.currentClass=p.find(N=>N.id==_),j(()=>{this.state.loading=!1})}return a(s),{lmclasses:s,state:i,updateStore:t,fetchClasses:c,checkClassRoute:a}},watch:{classId:function(e){e&&this.fetchClasses(e)}},async mounted(){console.log("LMClassView mounted",this.classId),this.fetchClasses(this.classId)},async updated(){console.log("LMClassView updated",this.classId),this.checkClassRoute(this.lmclasses)},components:{LMClassReleaseList:He},methods:{onScrollToTop(){var t,o;const e=(o=(t=this.$refs)==null?void 0:t.albumContainer)==null?void 0:o.querySelectorAll(".lm-album-release");if(e&&e.length>0){const s=e[0];s.scrollIntoView(),window.scrollY>100&&window.scrollBy(0,-81),s.classList.add("lm-release-highligt"),setTimeout(()=>s.classList.remove("lm-release-highligt"),1e3)}},onScrollToBottom(){var t,o;const e=(o=(t=this.$refs)==null?void 0:t.albumContainer)==null?void 0:o.querySelectorAll(".lm-album-release");if(e&&e.length>1){const s=e[e.length-1];s.scrollIntoView(),window.scrollBy(0,-81),s.classList.add("lm-release-highligt"),setTimeout(()=>s.classList.remove("lm-release-highligt"),1e3)}}}}),qe={class:"main-view"},Ee={class:"lm-class-navigation"},Fe={key:0,class:"album-container album-container-loading"},je={key:1,ref:"albumContainer",class:"album-container"};function Ge(e,t,o,s,r,l){const i=v("router-link"),a=v("LMClassReleaseList");return u(),d("div",qe,[n("ul",Ee,[(u(!0),d(g,null,y(e.lmclasses,c=>(u(),d("li",null,[f(i,{to:{name:"LM Class Releases",params:{classId:c.id}}},{default:S(()=>[h(m(c.short),1)]),_:2},1032,["to"])]))),256))]),e.state.loading?(u(),d("div",Fe,"Loading...")):(u(),d("div",je,[f(a,{lmclass:e.state.currentClass,onScrollToTop:e.onScrollToTop,onScrollToBottom:e.onScrollToBottom},null,8,["lmclass","onScrollToTop","onScrollToBottom"])],512))])}var Ue=C(Oe,[["render",Ge]]);const ze=M({setup(e){const t=G(),o=R(t.params);return{LMClassStore:Te,params:o}},watch:{$route:function(e){console.log("route changed!",e.params),this.params.classId=e.params.classId}},components:{DataProvider:Ce,LMClassView:Ue}}),Qe={class:"lesmills-home"};function We(e,t,o,s,r,l){const i=v("LMClassView"),a=v("DataProvider");return u(),d("div",Qe,[f(a,{defaultStore:e.LMClassStore},{default:S(()=>[f(i,{classId:e.params.classId},null,8,["classId"])]),_:1},8,["defaultStore"])])}var D=C(ze,[["render",We],["__scopeId","data-v-5be2d172"]]);const Ye=[{path:"/",name:"Home",component:fe},{path:"/class",name:"LM Classes",component:D},{path:"/class/:classId/releases/",name:"LM Class Releases",component:D}],Je=U({history:z(),routes:Ye}),Xe=Q(he);Xe.use(Je).mount("#app");