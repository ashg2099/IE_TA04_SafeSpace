<template>
  <nav class="navbar navbar-expand-md fixed-top bg-white border-bottom border-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        Safe-space
      </a>

      <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvas"
        aria-controls="offcanvas" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvas" aria-labelledby="offcanvasLabel">
        <div class="offcanvas-header">
          <h5 class="offcanvas-title" id="offcanvasLabel">Safe-space</h5>
          <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
          <ul class="navbar-nav ms-auto mb-2 mb-md-0">
            <li class="nav-item"><a class="nav-link" href="#">Tour</a></li>
            <li class="nav-item"><a class="nav-link" href="#">Product</a></li>
            <li class="nav-item"><a class="nav-link" href="#">Features</a></li>
            <li class="nav-item"><a class="nav-link" href="#">Enterprise</a></li>
            <li class="nav-item"><a class="nav-link" href="#">Support</a></li>
            <li class="nav-item"><a class="nav-link" href="#">Pricing</a></li>
          </ul>
        </div>
      </div>
    </div>
  </nav>

  <!-- 为固定导航栏添加间距，防止内容被覆盖 -->
  <div style="padding-top: 80px;"></div>
</template>

<style scoped>
.navbar {
  height: 80px;
  padding-top: 0;
  padding-bottom: 0;
}

.navbar-brand {
  font-size: 1.5rem;
  font-weight: bold;
}
</style>
