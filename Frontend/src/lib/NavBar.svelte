<script>
    let navLinks = [
      { text: 'Home', route: '/' },
      { text: 'Current Projects', route: '/projects' },
      { text: 'Project Map', route: '/projectmap' },
      { text: 'About', route: '/about' }
    ];
  </script>


<nav>
    <nav>
        <ul>
          {#each navLinks as link (link.text)}
            <li>
              <a href={link.route}>{link.text}</a>
            </li>
          {/each}
        </ul>
      </nav>
</nav>

<slot>

</slot>