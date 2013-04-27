  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>CS164-Class-Interpreter/grammar.py at master · hjjiang/CS164-Class-Interpreter · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="http://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <link rel="xhr-socket" href="/_sockets">
    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="QRwdnPBA5vCRnq9np0t8fsPsmeCSMR5m/pjA6l/Qqn4=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-21d1f919c9b16786238504ad1232b4937bbdd088.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-b702f2bd3370655be3cd89c1cd8cb00052d6a475.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-92d138f450f2960501e28397a2f63b0f100590f0.js" type="text/javascript"></script>
      <script src="https://a248.e.akamai.net/assets.github.com/assets/github-8b597885ade82d6a3d9108d93ea8e86b9f294d91.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="77a530946004f4df817ad3a299a913ed">

        <link data-pjax-transient rel='permalink' href='/hjjiang/CS164-Class-Interpreter/blob/e549b9d1d5d388e3a51a42feb1df46f36ff5e14f/grammar.py'>
    <meta property="og:title" content="CS164-Class-Interpreter"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/hjjiang/CS164-Class-Interpreter"/>
    <meta property="og:image" content="https://secure.gravatar.com/avatar/63c7d91916085620456f3bc721923008?s=420&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="CS164-Class-Interpreter - CS164 Class Interpreter"/>
    <meta property="twitter:card" content="summary"/>
    <meta property="twitter:site" content="@GitHub">
    <meta property="twitter:title" content="hjjiang/CS164-Class-Interpreter"/>

    <meta name="description" content="CS164-Class-Interpreter - CS164 Class Interpreter" />

  <link href="https://github.com/hjjiang/CS164-Class-Interpreter/commits/master.atom" rel="alternate" title="Recent Commits to CS164-Class-Interpreter:master" type="application/atom+xml" />

  </head>


  <body class="logged_out page-blob linux vis-public env-production  ">
    <div id="wrapper">

      

      
      
      

      
      <div class="header header-logged-out">
  <div class="container clearfix">

      <a class="header-logo-wordmark" href="https://github.com/">Github</a>

    <div class="header-actions">
        <a class="button primary" href="https://github.com/signup">Sign up for free</a>
      <a class="button" href="https://github.com/login?return_to=%2Fhjjiang%2FCS164-Class-Interpreter%2Fblob%2Fmaster%2Fgrammar.py">Sign in</a>
    </div>

      <ul class="top-nav">
          <li class="explore"><a href="https://github.com/explore">Explore GitHub</a></li>
        <li class="search"><a href="https://github.com/search">Search</a></li>
        <li class="features"><a href="https://github.com/features">Features</a></li>
          <li class="blog"><a href="https://github.com/blog">Blog</a></li>
      </ul>

  </div>
</div>


      

      


            <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="hentry">
        
        <div class="pagehead repohead instapaper_ignore readability-menu ">
          <div class="container">
            <div class="title-actions-bar">
              

<ul class="pagehead-actions">



    <li>
      <a href="/login?return_to=%2Fhjjiang%2FCS164-Class-Interpreter"
        class="minibutton js-toggler-target star-button entice tooltipped upwards"
        title="You must be signed in to use this feature" rel="nofollow">
        <span class="mini-icon mini-icon-star"></span>Star
      </a>
      <a class="social-count js-social-count" href="/hjjiang/CS164-Class-Interpreter/stargazers">
        2
      </a>
    </li>
    <li>
      <a href="/login?return_to=%2Fhjjiang%2FCS164-Class-Interpreter"
        class="minibutton js-toggler-target fork-button entice tooltipped upwards"
        title="You must be signed in to fork a repository" rel="nofollow">
        <span class="mini-icon mini-icon-fork"></span>Fork
      </a>
      <a href="/hjjiang/CS164-Class-Interpreter/network" class="social-count">
        0
      </a>
    </li>
</ul>

              <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
                <span class="repo-label"><span>public</span></span>
                <span class="mega-icon mega-icon-public-repo"></span>
                <span class="author vcard">
                  <a href="/hjjiang" class="url fn" itemprop="url" rel="author">
                  <span itemprop="title">hjjiang</span>
                  </a></span> /
                <strong><a href="/hjjiang/CS164-Class-Interpreter" class="js-current-repository">CS164-Class-Interpreter</a></strong>
              </h1>
            </div>

            
  <ul class="tabs">
    <li class="pulse-nav"><a href="/hjjiang/CS164-Class-Interpreter/pulse" highlight="pulse" rel="nofollow"><span class="mini-icon mini-icon-pulse"></span></a></li>
    <li><a href="/hjjiang/CS164-Class-Interpreter" class="selected" highlight="repo_source repo_downloads repo_commits repo_tags repo_branches">Code</a></li>
    <li><a href="/hjjiang/CS164-Class-Interpreter/network" highlight="repo_network">Network</a></li>
    <li><a href="/hjjiang/CS164-Class-Interpreter/pulls" highlight="repo_pulls">Pull Requests <span class='counter'>0</span></a></li>

      <li><a href="/hjjiang/CS164-Class-Interpreter/issues" highlight="repo_issues">Issues <span class='counter'>0</span></a></li>



    <li><a href="/hjjiang/CS164-Class-Interpreter/graphs" highlight="repo_graphs repo_contributors">Graphs</a></li>


  </ul>
  
<div class="tabnav">

  <span class="tabnav-right">
    <ul class="tabnav-tabs">
          <li><a href="/hjjiang/CS164-Class-Interpreter/tags" class="tabnav-tab" highlight="repo_tags">Tags <span class="counter blank">0</span></a></li>
    </ul>
    
  </span>

  <div class="tabnav-widget scope">


    <div class="select-menu js-menu-container js-select-menu js-branch-menu">
      <a class="minibutton select-menu-button js-menu-target" data-hotkey="w" data-ref="master">
        <span class="mini-icon mini-icon-branch"></span>
        <i>branch:</i>
        <span class="js-select-button">master</span>
      </a>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">

        <div class="select-menu-modal">
          <div class="select-menu-header">
            <span class="select-menu-title">Switch branches/tags</span>
            <span class="mini-icon mini-icon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-filters">
            <div class="select-menu-text-filter">
              <input type="text" id="commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
            </div>
            <div class="select-menu-tabs">
              <ul>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
                </li>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
                </li>
              </ul>
            </div><!-- /.select-menu-tabs -->
          </div><!-- /.select-menu-filters -->

          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="branches">

            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

                <div class="select-menu-item js-navigation-item selected">
                  <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                  <a href="/hjjiang/CS164-Class-Interpreter/blob/master/grammar.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" rel="nofollow" title="master">master</a>
                </div> <!-- /.select-menu-item -->
            </div>

              <div class="select-menu-no-results">Nothing to show</div>
          </div> <!-- /.select-menu-list -->


          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="tags">
            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

            </div>

            <div class="select-menu-no-results">Nothing to show</div>

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

  </div> <!-- /.scope -->

  <ul class="tabnav-tabs">
    <li><a href="/hjjiang/CS164-Class-Interpreter" class="selected tabnav-tab" highlight="repo_source">Files</a></li>
    <li><a href="/hjjiang/CS164-Class-Interpreter/commits/master" class="tabnav-tab" highlight="repo_commits">Commits</a></li>
    <li><a href="/hjjiang/CS164-Class-Interpreter/branches" class="tabnav-tab" highlight="repo_branches" rel="nofollow">Branches <span class="counter ">1</span></a></li>
  </ul>

</div>

  
  
  


            
          </div>
        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" class="container context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:276e97929b8866f9eea8191817688804 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:276e97929b8866f9eea8191817688804 -->


<div id="slider">
    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

        <div class="breadcrumb">
          <span class='bold'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/hjjiang/CS164-Class-Interpreter" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">CS164-Class-Interpreter</span></a></span></span><span class="separator"> / </span><strong class="final-path">grammar.py</strong> <span class="js-zeroclipboard zeroclipboard-button" data-clipboard-text="grammar.py" data-copied-hint="copied!" title="copy to clipboard"><span class="mini-icon mini-icon-clipboard"></span></span>
        </div>

      <a href="/hjjiang/CS164-Class-Interpreter/find/master" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>


        <div class="commit commit-loader file-history-tease js-deferred-content" data-url="/hjjiang/CS164-Class-Interpreter/contributors/master/grammar.py">
          Fetching contributors…

          <div class="participation">
            <p class="loader-loading"><img alt="Octocat-spinner-32-eaf2f5" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif?1360648847" width="16" /></p>
            <p class="loader-error">Cannot retrieve contributors at this time</p>
          </div>
        </div>

    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/hjjiang/CS164-Class-Interpreter/blob/e549b9d1d5d388e3a51a42feb1df46f36ff5e14f/grammar.py" data-title="CS164-Class-Interpreter/grammar.py at master · hjjiang/CS164-Class-Interpreter · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="mini-icon mini-icon-text-file"></b></span>
                <span class="mode" title="File Mode">file</span>
                  <span>259 lines (192 sloc)</span>
                <span>8.848 kb</span>
              </div>
              <div class="actions">
                <div class="button-group">
                      <a class="minibutton js-entice" href=""
                         data-entice="You must be signed in and on a branch to make or propose changes">Edit</a>
                  <a href="/hjjiang/CS164-Class-Interpreter/raw/master/grammar.py" class="button minibutton " id="raw-url">Raw</a>
                    <a href="/hjjiang/CS164-Class-Interpreter/blame/master/grammar.py" class="button minibutton ">Blame</a>
                  <a href="/hjjiang/CS164-Class-Interpreter/commits/master/grammar.py" class="button minibutton " rel="nofollow">History</a>
                </div><!-- /.button-group -->
              </div><!-- /.actions -->

            </div>
                <div class="blob-wrapper data type-python js-blob-data">
      <table class="file-code file-diff">
        <tr class="file-code-line">
          <td class="blob-line-nums">
            <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>

          </td>
          <td class="blob-line-code">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="c">##</span></div><div class='line' id='LC2'>&nbsp;<span class="c"># @file grammar.py</span></div><div class='line' id='LC3'>&nbsp;<span class="c">#</span></div><div class='line' id='LC4'>&nbsp;<span class="c"># $Id: grammar.py,v 1.7 2007/04/02 20:46:57 cgjones Exp $</span></div><div class='line' id='LC5'><span class="kn">import</span> <span class="nn">re</span><span class="o">,</span> <span class="nn">types</span></div><div class='line' id='LC6'><span class="kn">from</span> <span class="nn">sys</span> <span class="kn">import</span> <span class="n">stdout</span></div><div class='line' id='LC7'><br/></div><div class='line' id='LC8'><span class="k">class</span> <span class="nc">Production</span><span class="p">:</span></div><div class='line' id='LC9'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;</span></div><div class='line' id='LC10'><span class="sd">    LHS is the LHS symbol (redundancy beware: this symbol is also stored in the Rule)</span></div><div class='line' id='LC11'><span class="sd">    </span></div><div class='line' id='LC12'><span class="sd">    RHS is an array of symbols; e.g., [&quot;E&quot;, &quot;+&quot;, &quot;E&quot;].</span></div><div class='line' id='LC13'><br/></div><div class='line' id='LC14'><span class="sd">    ACTIONS is the set of actions associated with this production.  It</span></div><div class='line' id='LC15'><span class="sd">    is an array of texts of functions to execute either before</span></div><div class='line' id='LC16'><span class="sd">    evaluating a symbol (I-actions) or after evaluating all</span></div><div class='line' id='LC17'><span class="sd">    symbols in the RHS (S-action).  Each action corresponds to a</span></div><div class='line' id='LC18'><span class="sd">    symbol from RHS, and the final action is the optional</span></div><div class='line' id='LC19'><span class="sd">    S-action.  Each action can be None.</span></div><div class='line' id='LC20'><br/></div><div class='line' id='LC21'><span class="sd">    PREC is the precedence of this production among all the ones for</span></div><div class='line' id='LC22'><span class="sd">    this rule.</span></div><div class='line' id='LC23'><br/></div><div class='line' id='LC24'><span class="sd">    ASSOC is a terminal symbol whose precedence should be used</span></div><div class='line' id='LC25'><span class="sd">    in this rule, overriding that of any other terminals with</span></div><div class='line' id='LC26'><span class="sd">    associativity declarations.</span></div><div class='line' id='LC27'><br/></div><div class='line' id='LC28'><span class="sd">    RHSACTIONS is a list of (Symbol, Action) pairs.  Each Action</span></div><div class='line' id='LC29'><span class="sd">    will executed before its Symbol is evaluated.  The Actions can</span></div><div class='line' id='LC30'><span class="sd">    pass inherited attributes down the tree, allowing the use of</span></div><div class='line' id='LC31'><span class="sd">    L-attributed SDTs.</span></div><div class='line' id='LC32'><br/></div><div class='line' id='LC33'><span class="sd">    opPrec:</span></div><div class='line' id='LC34'><span class="sd">    opAssoc:</span></div><div class='line' id='LC35'><span class="sd">    &#39;&#39;&#39;</span> </div><div class='line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span> <span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">lhs</span><span class="p">,</span> <span class="n">rhs</span><span class="p">,</span> <span class="n">actions</span><span class="p">,</span> <span class="n">prec</span><span class="p">,</span> <span class="n">assoc</span><span class="p">):</span></div><div class='line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Create a new production&#39;&#39;&#39;</span></div><div class='line' id='LC38'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">LHS</span> <span class="o">=</span> <span class="n">lhs</span></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">RHS</span> <span class="o">=</span> <span class="n">rhs</span></div><div class='line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">actions</span> <span class="o">=</span> <span class="n">actions</span></div><div class='line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">prec</span> <span class="o">=</span> <span class="n">prec</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">assoc</span> <span class="o">=</span> <span class="n">assoc</span></div><div class='line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">opPrec</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">opAssoc</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">info</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC47'><br/></div><div class='line' id='LC48'><br/></div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">toString</span> <span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">invRenamedTerminals</span><span class="p">):</span></div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Print a representation of the production in the form</span></div><div class='line' id='LC51'><span class="sd">        LHS -&gt; RHS.  Token regexes are reintroduced using invRenamedTerminals.</span></div><div class='line' id='LC52'><span class="sd">        See Earley.preprocess for more information on this map.</span></div><div class='line' id='LC53'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">LHS</span><span class="o">+</span><span class="s">&quot; -&gt; &quot;</span><span class="o">+</span><span class="s">&quot; &quot;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">invRenamedTerminals</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">sym</span><span class="p">,</span><span class="n">sym</span><span class="p">)</span> <span class="k">for</span> <span class="n">sym</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">RHS</span><span class="p">])</span></div><div class='line' id='LC55'><br/></div><div class='line' id='LC56'><span class="k">class</span> <span class="nc">Rule</span><span class="p">:</span></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;A mapping from Symbol -&gt; [RHSs].</span></div><div class='line' id='LC58'><br/></div><div class='line' id='LC59'><span class="sd">    Also keeps track of associativity declarations for each</span></div><div class='line' id='LC60'><span class="sd">    production, and the precedences of ambiguous production (if any).</span></div><div class='line' id='LC61'><span class="sd">    &#39;&#39;&#39;</span></div><div class='line' id='LC62'><br/></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span> <span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">symbol</span><span class="p">):</span></div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Create a new rule for SYMBOL.&#39;&#39;&#39;</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">lhs</span> <span class="o">=</span> <span class="n">symbol</span></div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">productions</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC67'><br/></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__repr__</span> <span class="p">(</span><span class="bp">self</span><span class="p">):</span> <span class="k">return</span> <span class="nb">str</span> <span class="p">(</span><span class="bp">self</span><span class="p">)</span></div><div class='line' id='LC69'><br/></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__str__</span> <span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;&lt;grammar.Rule lhs=&quot;</span><span class="si">%s</span><span class="s">&quot; ...&gt;&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lhs</span><span class="p">)</span></div><div class='line' id='LC72'><br/></div><div class='line' id='LC73'><br/></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">dump</span> <span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">file</span><span class="o">=</span><span class="n">stdout</span><span class="p">,</span> <span class="n">i</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Print a pretty version of this rule to FILE at indent level I&#39;&#39;&#39;</span></div><div class='line' id='LC76'><br/></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">REGEX</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span> <span class="p">(</span><span class="s">&#39;a&#39;</span><span class="p">)</span>        <span class="c"># so we simulate isinstance()</span></div><div class='line' id='LC78'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="nb">file</span><span class="p">,</span> <span class="p">(</span><span class="n">i</span><span class="o">*</span><span class="s">&#39; &#39;</span><span class="p">)</span><span class="o">+</span><span class="s">&#39;(Rule </span><span class="si">%s</span><span class="s">&#39;</span><span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lhs</span><span class="p">)</span></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">i</span> <span class="o">+=</span> <span class="mi">4</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">prod</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">productions</span><span class="p">:</span></div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="nb">file</span><span class="p">,</span> <span class="p">(</span><span class="n">i</span><span class="o">*</span><span class="s">&#39; &#39;</span><span class="p">)</span><span class="o">+</span><span class="s">&#39;(production [&#39;</span><span class="p">,</span></div><div class='line' id='LC83'><br/></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">sym</span> <span class="ow">in</span> <span class="n">prod</span><span class="o">.</span><span class="n">RHS</span><span class="p">:</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">sym</span> <span class="o">==</span> <span class="n">Grammar</span><span class="o">.</span><span class="n">EPSILON</span><span class="p">:</span></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="nb">file</span><span class="p">,</span> <span class="s">&#39;(epsilon),&#39;</span><span class="p">,</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="nb">type</span> <span class="p">(</span><span class="n">sym</span><span class="p">)</span> <span class="o">==</span> <span class="nb">type</span> <span class="p">(</span><span class="n">REGEX</span><span class="p">):</span></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="nb">file</span><span class="p">,</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s">,&#39;</span><span class="o">%</span> <span class="p">(</span><span class="n">sym</span><span class="o">.</span><span class="n">pattern</span><span class="p">),</span></div><div class='line' id='LC89'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="nb">file</span><span class="p">,</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s">,&#39;</span><span class="o">%</span> <span class="p">(</span><span class="n">sym</span><span class="p">),</span></div><div class='line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="nb">file</span><span class="p">,</span> <span class="s">&#39;]&#39;</span></div><div class='line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">prod</span><span class="o">.</span><span class="n">prec</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="nb">file</span><span class="p">,</span> <span class="p">((</span><span class="n">i</span><span class="o">+</span><span class="mi">4</span><span class="p">)</span><span class="o">*</span><span class="s">&#39; &#39;</span><span class="p">)</span><span class="o">+</span><span class="s">&#39;(precedence </span><span class="si">%d</span><span class="s">)&#39;</span><span class="o">%</span> <span class="p">(</span><span class="n">prod</span><span class="o">.</span><span class="n">prec</span><span class="p">)</span></div><div class='line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">prod</span><span class="o">.</span><span class="n">assoc</span><span class="p">:</span></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="nb">file</span><span class="p">,</span> <span class="p">((</span><span class="n">i</span><span class="o">+</span><span class="mi">4</span><span class="p">)</span><span class="o">*</span><span class="s">&#39; &#39;</span><span class="p">)</span><span class="o">+</span><span class="s">&#39;(assoc </span><span class="si">%s</span><span class="s">)&#39;</span><span class="o">%</span> <span class="p">(</span><span class="n">prod</span><span class="o">.</span><span class="n">assoc</span><span class="o">.</span><span class="n">pattern</span><span class="p">)</span></div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">prod</span><span class="o">.</span><span class="n">actions</span><span class="p">:</span></div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="nb">file</span><span class="p">,</span> <span class="p">((</span><span class="n">i</span><span class="o">+</span><span class="mi">4</span><span class="p">)</span><span class="o">*</span><span class="s">&#39; &#39;</span><span class="p">)</span><span class="o">+</span><span class="s">&#39;(action {</span><span class="si">%s</span><span class="s">})&#39;</span><span class="o">%</span> <span class="p">(</span><span class="n">prod</span><span class="o">.</span><span class="n">actions</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="nb">file</span><span class="p">,</span> <span class="p">(</span><span class="n">i</span><span class="o">*</span><span class="s">&#39; &#39;</span><span class="p">)</span><span class="o">+</span> <span class="s">&#39;)&#39;</span></div><div class='line' id='LC100'><br/></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">i</span> <span class="o">-=</span> <span class="mi">4</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="nb">file</span><span class="p">,</span> <span class="p">(</span><span class="n">i</span><span class="o">*</span><span class="s">&#39; &#39;</span><span class="p">)</span><span class="o">+</span><span class="s">&#39;)&#39;</span></div><div class='line' id='LC103'><br/></div><div class='line' id='LC104'><br/></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">addProduction</span> <span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">rhs</span><span class="p">,</span> <span class="n">actions</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">prec</span><span class="o">=-</span><span class="mi">1</span><span class="p">,</span> <span class="n">assoc</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Add a production self.lhs -&gt; RHS, with an optional precedence,</span></div><div class='line' id='LC107'><span class="sd">        semantic action, and associativity override.</span></div><div class='line' id='LC108'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC109'><br/></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># CYK TODO: make sure changing Production from a dict to an object</span></div><div class='line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># did not break the cyk parser.</span></div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># (old) CYK code</span></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># self.productions.append (</span></div><div class='line' id='LC115'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#    { &#39;rhs&#39;: tuple(rhs), &#39;actions&#39;: actions, &#39;prec&#39;: prec,</span></div><div class='line' id='LC116'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#      &#39;assoc&#39;: assoc,})</span></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">productions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Production</span><span class="p">(</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">lhs</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">rhs</span><span class="p">),</span></div><div class='line' id='LC120'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">actions</span><span class="p">,</span> <span class="n">prec</span><span class="p">,</span> <span class="n">assoc</span><span class="p">))</span></div><div class='line' id='LC121'><br/></div><div class='line' id='LC122'><span class="c">##-----------------------------------------------------------------------------</span></div><div class='line' id='LC123'><br/></div><div class='line' id='LC124'><span class="k">class</span> <span class="nc">Grammar</span><span class="p">:</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;The data structure representing an abstract grammar.&#39;&#39;&#39;</span></div><div class='line' id='LC126'><br/></div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">EPSILON</span> <span class="o">=</span> <span class="s">&#39;_&#39;</span><span class="p">,</span></div><div class='line' id='LC128'><br/></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LEFT_ASSOCIATIVE</span> <span class="o">=</span> <span class="s">&#39;left&#39;</span><span class="p">,</span></div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">RIGHT_ASSOCIATIVE</span> <span class="o">=</span> <span class="s">&#39;right&#39;</span><span class="p">,</span></div><div class='line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span> <span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC133'>		<span class="sd">&#39;&#39;&#39;Create a new Grammar.&#39;&#39;&#39;</span></div><div class='line' id='LC134'>		<span class="bp">self</span><span class="o">.</span><span class="n">rules</span> <span class="o">=</span> <span class="p">[]</span>                 <span class="c"># list of Rules</span></div><div class='line' id='LC135'>		<span class="bp">self</span><span class="o">.</span><span class="n">startSymbol</span> <span class="o">=</span> <span class="s">&#39;&#39;</span>           <span class="c"># the start symbol of this grammar</span></div><div class='line' id='LC136'>		<span class="bp">self</span><span class="o">.</span><span class="n">imports</span> <span class="o">=</span> <span class="p">[]</span>               <span class="c"># modules to be imported</span></div><div class='line' id='LC137'>		<span class="bp">self</span><span class="o">.</span><span class="n">ignores</span> <span class="o">=</span> <span class="p">[]</span>               <span class="c"># terminals to be ignored</span></div><div class='line' id='LC138'>		<span class="bp">self</span><span class="o">.</span><span class="n">optionals</span> <span class="o">=</span> <span class="p">[]</span>             <span class="c"># &quot;optional&quot; terminal symbols</span></div><div class='line' id='LC139'><br/></div><div class='line' id='LC140'>		<span class="bp">self</span><span class="o">.</span><span class="n">__opAssocDecls</span> <span class="o">=</span> <span class="p">[]</span>        <span class="c"># operator associativity declarations</span></div><div class='line' id='LC141'>		<span class="bp">self</span><span class="o">.</span><span class="n">__currOpPrec</span> <span class="o">=</span> <span class="mi">0</span>           <span class="c"># the current operator precedence</span></div><div class='line' id='LC142'><br/></div><div class='line' id='LC143'>		<span class="bp">self</span><span class="o">.</span><span class="n">__symbol2rule</span> <span class="o">=</span> <span class="p">{}</span>		<span class="c"># map symbols to their Rule</span></div><div class='line' id='LC144'><br/></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__repr__</span> <span class="p">(</span><span class="bp">self</span><span class="p">):</span> <span class="k">return</span> <span class="nb">str</span> <span class="p">(</span><span class="bp">self</span><span class="p">)</span></div><div class='line' id='LC146'><br/></div><div class='line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__str__</span> <span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;&lt;grammar.Grammar startSymbol=&quot;</span><span class="si">%s</span><span class="s">&quot; ...&gt;&#39;</span><span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">startSymbol</span><span class="p">)</span></div><div class='line' id='LC149'><br/></div><div class='line' id='LC150'><br/></div><div class='line' id='LC151'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">dump</span> <span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">file</span><span class="o">=</span><span class="n">stdout</span><span class="p">):</span></div><div class='line' id='LC152'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Print a pretty version of this grammar to FILE&#39;&#39;&#39;</span></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="nb">file</span><span class="p">,</span> <span class="s">&#39;(Grammar&#39;</span></div><div class='line' id='LC154'><br/></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="nb">file</span><span class="p">,</span> <span class="p">(</span><span class="mi">4</span><span class="o">*</span><span class="s">&#39; &#39;</span><span class="p">)</span><span class="o">+</span><span class="s">&#39;(Declarations&#39;</span></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">mod</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">imports</span><span class="p">:</span></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="nb">file</span><span class="p">,</span> <span class="p">(</span><span class="mi">8</span><span class="o">*</span><span class="s">&#39; &#39;</span><span class="p">)</span><span class="o">+</span><span class="s">&#39;(import </span><span class="si">%s</span><span class="s">)&#39;</span><span class="o">%</span> <span class="p">(</span><span class="n">mod</span><span class="p">)</span></div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="p">(</span><span class="n">op</span><span class="p">,</span> <span class="n">prec</span><span class="p">,</span> <span class="n">assoc</span><span class="p">)</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__opAssocDecls</span><span class="p">:</span></div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="nb">file</span><span class="p">,</span> <span class="p">(</span><span class="mi">8</span><span class="o">*</span><span class="s">&#39; &#39;</span><span class="p">)</span><span class="o">+</span><span class="s">&#39;(assoc </span><span class="si">%s</span><span class="s"> </span><span class="si">%d</span><span class="s"> </span><span class="si">%s</span><span class="s">)&#39;</span><span class="o">%</span> <span class="p">(</span><span class="n">op</span><span class="o">.</span><span class="n">pattern</span><span class="p">,</span> <span class="n">prec</span><span class="p">,</span> <span class="n">assoc</span><span class="p">)</span></div><div class='line' id='LC160'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="nb">file</span><span class="p">,</span> <span class="p">(</span><span class="mi">4</span><span class="o">*</span><span class="s">&#39; &#39;</span><span class="p">)</span><span class="o">+</span><span class="s">&#39;)&#39;</span></div><div class='line' id='LC161'><br/></div><div class='line' id='LC162'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="nb">file</span><span class="p">,</span> <span class="p">(</span><span class="mi">4</span><span class="o">*</span><span class="s">&#39; &#39;</span><span class="p">)</span><span class="o">+</span><span class="s">&#39;(Rules&#39;</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">rule</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">rules</span><span class="p">:</span></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rule</span><span class="o">.</span><span class="n">dump</span> <span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="mi">8</span><span class="p">)</span></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="nb">file</span><span class="p">,</span> <span class="p">(</span><span class="mi">4</span><span class="o">*</span><span class="s">&#39; &#39;</span><span class="p">)</span><span class="o">+</span><span class="s">&#39;)&#39;</span></div><div class='line' id='LC166'><br/></div><div class='line' id='LC167'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="nb">file</span><span class="p">,</span> <span class="p">(</span><span class="mi">4</span><span class="o">*</span><span class="s">&#39; &#39;</span><span class="p">)</span><span class="o">+</span><span class="s">&#39;(StartSymbol </span><span class="si">%s</span><span class="s">)&#39;</span><span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">startSymbol</span><span class="p">)</span></div><div class='line' id='LC168'><br/></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="nb">file</span><span class="p">,</span> <span class="s">&#39;)&#39;</span></div><div class='line' id='LC170'><br/></div><div class='line' id='LC171'><br/></div><div class='line' id='LC172'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setStartSymbol</span> <span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">startSymbol</span><span class="p">):</span></div><div class='line' id='LC173'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Set the start symbol of this grammar.&#39;&#39;&#39;</span></div><div class='line' id='LC174'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">startSymbol</span> <span class="o">=</span> <span class="n">startSymbol</span></div><div class='line' id='LC175'><br/></div><div class='line' id='LC176'><br/></div><div class='line' id='LC177'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">declareImport</span> <span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">module</span><span class="p">):</span></div><div class='line' id='LC178'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Declare that MODULE should be imported by this grammar.&#39;&#39;&#39;</span></div><div class='line' id='LC179'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">imports</span><span class="o">.</span><span class="n">append</span> <span class="p">(</span><span class="n">module</span><span class="p">)</span></div><div class='line' id='LC180'><br/></div><div class='line' id='LC181'><br/></div><div class='line' id='LC182'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">declareIgnore</span> <span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">regex</span><span class="p">):</span></div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Declare that REGEX should be ignored while tokenizing.&#39;&#39;&#39;</span></div><div class='line' id='LC184'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">ignores</span><span class="o">.</span><span class="n">append</span> <span class="p">(</span><span class="n">regex</span><span class="p">)</span></div><div class='line' id='LC185'><br/></div><div class='line' id='LC186'><br/></div><div class='line' id='LC187'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">declareOptional</span> <span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sym</span><span class="p">,</span> <span class="n">regex</span><span class="p">):</span></div><div class='line' id='LC188'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Declare that if REGEX is matched in the input, it should receive</span></div><div class='line' id='LC189'><span class="sd">        a self-edge with symbol SYM.&#39;&#39;&#39;</span></div><div class='line' id='LC190'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">optionals</span><span class="o">.</span><span class="n">append</span> <span class="p">((</span><span class="n">sym</span><span class="p">,</span> <span class="n">regex</span><span class="p">))</span></div><div class='line' id='LC191'><br/></div><div class='line' id='LC192'><br/></div><div class='line' id='LC193'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">declareOperatorAssocs</span> <span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">operators</span><span class="p">,</span> <span class="n">assoc</span><span class="p">):</span></div><div class='line' id='LC194'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Declare the associativity of the sequence OPERATORS to be ASSOC.</span></div><div class='line' id='LC195'><br/></div><div class='line' id='LC196'><span class="sd">        Also sets the precedence of these operators; the last set of</span></div><div class='line' id='LC197'><span class="sd">        operators passed to declareAssociativities() will have highest</span></div><div class='line' id='LC198'><span class="sd">        precedence, and so on.</span></div><div class='line' id='LC199'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC200'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">op</span> <span class="ow">in</span> <span class="n">operators</span><span class="p">:</span></div><div class='line' id='LC201'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">__opAssocDecls</span><span class="o">.</span><span class="n">append</span> <span class="p">((</span><span class="n">op</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">__currOpPrec</span><span class="p">,</span> <span class="n">assoc</span><span class="p">))</span></div><div class='line' id='LC202'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">__currOpPrec</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC203'><br/></div><div class='line' id='LC204'><br/></div><div class='line' id='LC205'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">addRule</span> <span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">rule</span><span class="p">):</span></div><div class='line' id='LC206'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Add RULE to the set of rules for this grammar.&#39;&#39;&#39;</span></div><div class='line' id='LC207'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">rules</span><span class="o">.</span><span class="n">append</span> <span class="p">(</span><span class="n">rule</span><span class="p">)</span></div><div class='line' id='LC208'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">__symbol2rule</span><span class="p">[</span><span class="n">rule</span><span class="o">.</span><span class="n">lhs</span><span class="p">]</span> <span class="o">=</span> <span class="n">rule</span></div><div class='line' id='LC209'><br/></div><div class='line' id='LC210'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getAssocDecls</span> <span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC211'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Fetch the operators with associativity declarations.  Returns</span></div><div class='line' id='LC212'><span class="sd">        the list [(operator, precedence, associativity)]</span></div><div class='line' id='LC213'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC214'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__opAssocDecls</span></div><div class='line' id='LC215'><br/></div><div class='line' id='LC216'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">symbol</span><span class="p">):</span></div><div class='line' id='LC217'>	<span class="sd">&#39;&#39;&#39;Return the rule for the ninterminal symbol, or None if symbol is not defined&#39;&#39;&#39;</span></div><div class='line' id='LC218'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__symbol2rule</span><span class="p">[</span><span class="n">symbol</span><span class="p">]</span></div><div class='line' id='LC219'><br/></div><div class='line' id='LC220'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">validate</span> <span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC221'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Run semantic checks against this grammar and its</span></div><div class='line' id='LC222'><span class="sd">        constituent rules.  Returns the tuple (valid?, message).</span></div><div class='line' id='LC223'><br/></div><div class='line' id='LC224'><span class="sd">        &quot;valid?&quot; is True if the grammar is valid, False otherwise.</span></div><div class='line' id='LC225'><br/></div><div class='line' id='LC226'><span class="sd">        &quot;message&quot; is a description of the semantic validations, and is</span></div><div class='line' id='LC227'><span class="sd">        only interesting when valid? is False.</span></div><div class='line' id='LC228'><span class="sd">        &#39;&#39;&#39;</span></div><div class='line' id='LC229'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lhss</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC230'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Seed LHSes with optional symbols</span></div><div class='line' id='LC231'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">sym</span><span class="p">,</span> <span class="n">regex</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">optionals</span><span class="p">:</span></div><div class='line' id='LC232'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lhss</span><span class="p">[</span><span class="n">sym</span><span class="p">]</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC233'><br/></div><div class='line' id='LC234'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Check property 1: no multiple definitions</span></div><div class='line' id='LC235'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">rule</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">rules</span><span class="p">:</span></div><div class='line' id='LC236'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">lhss</span><span class="o">.</span><span class="n">get</span> <span class="p">(</span><span class="n">rule</span><span class="o">.</span><span class="n">lhs</span><span class="p">,</span> <span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC237'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">(</span><span class="bp">False</span><span class="p">,</span> <span class="s">&#39;nonterminal </span><span class="si">%s</span><span class="s"> multiply defined&#39;</span><span class="o">%</span><span class="p">(</span><span class="n">rule</span><span class="o">.</span><span class="n">lhs</span><span class="p">))</span></div><div class='line' id='LC238'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC239'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lhss</span><span class="p">[</span><span class="n">rule</span><span class="o">.</span><span class="n">lhs</span><span class="p">]</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC240'><br/></div><div class='line' id='LC241'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Check property 2: no undefined symbols</span></div><div class='line' id='LC242'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">rule</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">rules</span><span class="p">:</span></div><div class='line' id='LC243'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">prod</span> <span class="ow">in</span> <span class="n">rule</span><span class="o">.</span><span class="n">productions</span><span class="p">:</span></div><div class='line' id='LC244'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">sym</span> <span class="ow">in</span> <span class="n">prod</span><span class="o">.</span><span class="n">RHS</span><span class="p">:</span></div><div class='line' id='LC245'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="nb">isinstance</span> <span class="p">(</span><span class="n">sym</span><span class="p">,</span> <span class="n">types</span><span class="o">.</span><span class="n">StringType</span><span class="p">)</span></div><div class='line' id='LC246'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ow">and</span> <span class="ow">not</span> <span class="n">lhss</span><span class="o">.</span><span class="n">get</span> <span class="p">(</span><span class="n">sym</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></div><div class='line' id='LC247'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ow">and</span> <span class="p">(</span><span class="n">sym</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">Grammar</span><span class="o">.</span><span class="n">EPSILON</span><span class="p">)):</span></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">(</span><span class="bp">False</span><span class="p">,</span> <span class="s">&#39;symbol &quot;</span><span class="si">%s</span><span class="s">&quot; not defined&#39;</span><span class="o">%</span> <span class="p">(</span><span class="n">sym</span><span class="p">))</span></div><div class='line' id='LC249'><br/></div><div class='line' id='LC250'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">(</span><span class="bp">True</span><span class="p">,</span> <span class="s">&#39;valid&#39;</span><span class="p">)</span></div><div class='line' id='LC251'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC252'><span class="c">##-----------------------------------------------------------------------------</span></div><div class='line' id='LC253'><br/></div><div class='line' id='LC254'><span class="k">def</span> <span class="nf">main</span> <span class="p">():</span></div><div class='line' id='LC255'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC256'><br/></div><div class='line' id='LC257'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span></div><div class='line' id='LC258'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">main</span> <span class="p">()</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>

        <a href="#jump-to-line" rel="facebox" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
        <div id="jump-to-line" style="display:none">
          <h2>Jump to Line</h2>
          <form accept-charset="UTF-8" class="js-jump-to-line-form">
            <input class="textfield js-jump-to-line-field" type="text">
            <div class="full-button">
              <button type="submit" class="button">Go</button>
            </div>
          </form>
        </div>

      </div>
    </div>
</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif?1360648847" height="64" width="64">
</div>


        </div>
      </div>
      <div class="context-overlay"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer">
  <div class="container clearfix">

      <dl class="footer_nav">
        <dt>GitHub</dt>
        <dd><a href="https://github.com/about">About us</a></dd>
        <dd><a href="https://github.com/blog">Blog</a></dd>
        <dd><a href="https://github.com/contact">Contact &amp; support</a></dd>
        <dd><a href="http://enterprise.github.com/">GitHub Enterprise</a></dd>
        <dd><a href="http://status.github.com/">Site status</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Applications</dt>
        <dd><a href="http://mac.github.com/">GitHub for Mac</a></dd>
        <dd><a href="http://windows.github.com/">GitHub for Windows</a></dd>
        <dd><a href="http://eclipse.github.com/">GitHub for Eclipse</a></dd>
        <dd><a href="http://mobile.github.com/">GitHub mobile apps</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Services</dt>
        <dd><a href="http://get.gaug.es/">Gauges: Web analytics</a></dd>
        <dd><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></dd>
        <dd><a href="https://gist.github.com">Gist: Code snippets</a></dd>
        <dd><a href="http://jobs.github.com/">Job board</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Documentation</dt>
        <dd><a href="http://help.github.com/">GitHub Help</a></dd>
        <dd><a href="http://developer.github.com/">Developer API</a></dd>
        <dd><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></dd>
        <dd><a href="http://pages.github.com/">GitHub Pages</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>More</dt>
        <dd><a href="http://training.github.com/">Training</a></dd>
        <dd><a href="https://github.com/edu">Students &amp; teachers</a></dd>
        <dd><a href="http://shop.github.com">The Shop</a></dd>
        <dd><a href="/plans">Plans &amp; pricing</a></dd>
        <dd><a href="http://octodex.github.com/">The Octodex</a></dd>
      </dl>

      <hr class="footer-divider">


    <p class="right">&copy; 2013 <span title="0.09561s from fe4.rs.github.com">GitHub</span>, Inc. All rights reserved.</p>
    <a class="left" href="https://github.com/">
      <span class="mega-icon mega-icon-invertocat"></span>
    </a>
    <ul id="legal">
        <li><a href="https://github.com/site/terms">Terms of Service</a></li>
        <li><a href="https://github.com/site/privacy">Privacy</a></li>
        <li><a href="https://github.com/security">Security</a></li>
    </ul>

  </div><!-- /.container -->

</div><!-- /.#footer -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/hjjiang/CS164-Class-Interpreter/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-icon mega-icon-normalscreen"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="mini-icon mini-icon-brightness"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="mini-icon mini-icon-exclamation"></span>
      Something went wrong with that request. Please try again.
      <a href="#" class="mini-icon mini-icon-remove-close ajax-error-dismiss"></a>
    </div>

    
    
    <span id='server_response_time' data-time='0.09616' data-host='fe4'></span>
    
  </body>
</html>

